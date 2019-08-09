from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class WorkspaceGroupsStream(BaseStream):
    NAME = 'WorkspaceGroupsStream'
    API_METHOD = 'GET'
    TABLE = 'workspace_groups'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/workspace_groups.json'

    @property
    def response_key(self):
        return 'workspace_groups'
