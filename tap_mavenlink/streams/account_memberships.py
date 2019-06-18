from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class AccountMembershipsStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'account_memberships'
    KEY_PROPERTIES = ['id']

    # Remove this line to enable this stream after adding a
    # JSON Schema in the schemas/ directory
    ENABLED = True

    # Remove this line to prevent the output from showing in
    # stdout once a json schema has been created for this stream
    PRINT_SAMPLE = True

    @property
    def path(self):
        return '/account_memberships.json'

    @property
    def response_key(self):
        return 'account_memberships'

    @property
    def include(self):
        return [
            'default_role',
        ]

