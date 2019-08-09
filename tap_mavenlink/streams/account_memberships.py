from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class AccountMembershipsStream(BaseStream):
    NAME = 'AccountMembershipsStream'
    API_METHOD = 'GET'
    TABLE = 'account_memberships'
    KEY_PROPERTIES = ['id']

    def extra_params(self):
        return {
            "only_active": "false"
        }
        
    @property
    def path(self):
        return '/account_memberships.json'

    @property
    def response_key(self):
        return 'account_memberships'
