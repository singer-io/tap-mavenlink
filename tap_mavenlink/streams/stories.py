
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class StoriesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'stories'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/stories.json'

    @property
    def response_key(self):
        return 'stories'
