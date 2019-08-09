from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class WorkspacesStream(BaseStream):
    NAME = 'WorkspacesStream'
    API_METHOD = 'GET'
    TABLE = 'workspaces'
    KEY_PROPERTIES = ['id']

    def extra_params(self):
        return {
            "include": "workspace_groups,participants,participations,custom_field_values",
            "include_archived": "true"
        }

    @property
    def path(self):
        return '/workspaces.json'

    @property
    def response_key(self):
        return 'workspaces'
