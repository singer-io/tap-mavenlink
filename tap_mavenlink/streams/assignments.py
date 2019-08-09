from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class AssignmentsStream(BaseStream):
    NAME = 'AssignmentsStream'
    API_METHOD = 'GET'
    TABLE = 'assignments'
    KEY_PROPERTIES = ['id']
    
    def extra_params(self):
        return {
            "in_unarchived_workspaces": "false",
            "in_unarchived_stories": "false"
        }
        
    @property
    def path(self):
        return '/assignments.json'

    @property
    def response_key(self):
        return 'assignments'
