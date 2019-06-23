
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class PostsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'posts'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/posts.json'

    @property
    def response_key(self):
        return 'posts'
