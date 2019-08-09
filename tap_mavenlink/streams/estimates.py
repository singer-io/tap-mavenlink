
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class EstimatesStream(BaseStream):
    NAME = 'EstimatesStream'
    API_METHOD = 'GET'
    TABLE = 'estimates'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/estimates.json'

    @property
    def response_key(self):
        return 'estimates'
