
from tap_mavenlink.streams.base import ResourceSubStream
from tap_mavenlink.cache import resources as ResourceCache
import singer

LOGGER = singer.get_logger()  # noqa


class EstimatesResourcesStream(ResourceSubStream):
    NAME = 'EstimatesResourcesStream'
    API_METHOD = 'GET'
    TABLE = 'estimate_scenario_resources'
    PARENT = 'estimate_scenarios'
    KEY_PROPERTIES = ['id']

    def get_extra(self, parent_id):
        return {"estimate_scenario_id": parent_id}

    def get_params(self, pk, page_number=1, per_page=200):
        return {
            'page': page_number,
            'per_page': per_page,
            'estimate_scenario_id': pk
        }

    @property
    def path(self):
        return '/estimate_scenario_resources.json'

    @property
    def response_key(self):
        return 'estimate_scenario_resources'
