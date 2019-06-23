
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class TimeEntriesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'time_entries'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/time_entries.json'

    @property
    def response_key(self):
        return 'time_entries'
