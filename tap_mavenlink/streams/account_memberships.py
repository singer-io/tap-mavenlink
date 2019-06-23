from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class AccountMembershipsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'account_memberships'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/account_memberships.json'

    @property
    def response_key(self):
        return 'account_memberships'
