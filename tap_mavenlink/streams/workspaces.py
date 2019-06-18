from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class WorkspacesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'workspaces'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/workspaces.json'

    @property
    def response_key(self):
        return 'workspaces'

    @property
    def include(self):
        return [
            'workspace_groups',
            'timesheet_submissions'
        ]
