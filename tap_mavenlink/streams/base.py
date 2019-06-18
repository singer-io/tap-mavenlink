import math
import pytz
import singer
import singer.utils
import singer.metrics

from datetime import timedelta, datetime

from tap_mavenlink.config import get_config_start_date
from tap_mavenlink.state import incorporate, save_state, \
    get_last_record_value_for_table

from tap_framework.streams import BaseStream as base


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ['id']
    ENABLED = True
    PRINT_SAMPLE = False

    def get_url(self):
        return 'https://api.mavenlink.com/api/v1{}'.format(self.path)

    @property
    def include(self):
        return []

    def get_params(self, page_number, per_page):
        params = {
            'page': page_number,
            'per_page': per_page
        }

        if len(self.include) > 0:
            params['include'] = ','.join(self.include)

        return params

    def sync_paginated(self, url):
        table = self.TABLE

        LOGGER.info('Syncing data for {}'.format(table))
        url = self.get_url()

        page_number = 1
        per_page = 10 # TODO : Revert to 200

        all_resources = []
        while True:
            params = self.get_params(page_number, per_page)
            result = self.client.make_request(url, self.API_METHOD, params=params)
            transformed = self.get_stream_data(result)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(data))
                all_resources.extend(data)

            total_pages = result['meta']['page_count']
            LOGGER.info('Synced page {} of {} for {}'.format(page_number, total_pages, self.TABLE))

            if page_number == total_pages:
                break
            else:
                page_number += 1

        save_state(self.state)
        return self.state

    def record_hook(self, i, record):
        if self.PRINT_SAMPLE and i % 10 == 0:
            LOGGER.info("SAMPLE {}: {}".format(i, record))
        return record

    def get_stream_data(self, result):
        payload_dict = result[self.response_key]
        payload_values = payload_dict.values()

        transformed = []
        for i, record in enumerate(payload_values):
            self.record_hook(i, record)
            transformed.append(self.transform_record(record))

        return transformed
