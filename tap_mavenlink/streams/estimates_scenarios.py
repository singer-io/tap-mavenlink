
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class EstimatesScenariosStream(BaseStream):
    NAME = 'EstimatesScenariosStream'
    API_METHOD = 'GET'
    TABLE = 'estimate_scenarios'
    KEY_PROPERTIES = ['id']
    CACHE = True

    @property
    def path(self):
        return '/estimate_scenarios.json'

    @property
    def response_key(self):
        return 'estimate_scenarios'
