
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class UsersStream(BaseStream):
    NAME = 'UsersStream'
    API_METHOD = 'GET'
    TABLE = 'users'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/users.json'

    @property
    def response_key(self):
        return 'users'
