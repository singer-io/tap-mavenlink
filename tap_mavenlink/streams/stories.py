
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class StoriesStream(BaseStream):
    NAME = 'StoriesStream'
    API_METHOD = 'GET'
    TABLE = 'stories'
    KEY_PROPERTIES = ['id']
    
    def extra_params(self):
        return {
            "show_archived": "true",
            "show_deleted": "true",
            "show_from_archived_workspaces": "true"
        }

    @property
    def path(self):
        return '/stories.json'

    @property
    def response_key(self):
        return 'stories'
