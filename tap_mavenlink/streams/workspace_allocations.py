from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class WorkspaceAllocationsStream(BaseStream):
    NAME = 'WorkspaceAllocationsStream'
    API_METHOD = 'GET'
    TABLE = 'workspace_allocations'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/workspace_allocations.json'

    @property
    def response_key(self):
        return 'workspace_allocations'
