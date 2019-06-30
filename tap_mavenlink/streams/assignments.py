from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class AssignmentsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'assignments'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/assignments.json'

    @property
    def response_key(self):
        return 'assignments'
