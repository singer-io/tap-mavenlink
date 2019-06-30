import math
import pytz
import singer
import singer.utils
import singer.metrics

from datetime import timedelta, datetime

from tap_mavenlink.cache import resources as ResourceCache
from tap_mavenlink.config import get_config_start_date
from tap_mavenlink.state import incorporate, save_state, \
    get_last_record_value_for_table

from tap_framework.streams import BaseStream as base


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']
    CACHE = False

    def get_extra(self, parent_id):
        return {}

    def get_url(self):
        return 'https://api.mavenlink.com/api/v1{}'.format(self.path)

    def extra_params(self):
        return {}

    def get_params(self, page_number=1, per_page=200):
        params = {
            'page': page_number,
            'per_page': per_page
        }

        params.update(self.extra_params())
        return params

    def sync_data(self):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        self.sync_paginated(self.get_params(), {})

    def sync_paginated(self, params, extra):
        table = self.TABLE
        url = self.get_url()

        while True:
            result = self.client.make_request(url, self.API_METHOD, params=params)
            transformed = self.get_stream_data(result, extra)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))

            page_number = params['page']
            total_pages = result['meta']['page_count']
            LOGGER.info('Synced page {} of {} for {}'.format(page_number, total_pages, self.TABLE))

            if page_number >= total_pages:
                break
            else:
                params['page'] += 1

    def get_stream_data(self, result, extra):
        payload_dict = result[self.response_key]
        payload_values = payload_dict.values()

        transformed = []
        for i, record in enumerate(payload_values):
            record.update(extra)
            record = self.transform_record(record)
            if self.CACHE:
                pk = record['id']
                ResourceCache[self.TABLE].add(pk)
            transformed.append(record)

        return transformed


class ResourceSubStream(BaseStream):

    def sync_data(self):
        table = self.TABLE

        for pk in ResourceCache[self.PARENT]:
            params = self.get_params(pk)
            LOGGER.info('Syncing data for {} (pk={})'.format(table, pk))
            extra = self.get_extra(pk)
            self.sync_paginated(params, extra=extra)
