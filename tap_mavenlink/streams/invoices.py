from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class InvoicesStream(BaseStream):
    API_METHOD = 'GET'
    TABLE = 'invoices'
    KEY_PROPERTIES = ['id']

    # Remove this line to enable this stream after adding a
    # JSON Schema in the schemas/ directory
    ENABLED = False

    # Remove this line to prevent the output from showing in
    # stdout once a json schema has been created for this stream
    PRINT_SAMPLE = True

    @property
    def path(self):
        return '/invoices.json'

    @property
    def response_key(self):
        return 'invoices'

    @property
    def include(self):
        return [
            'additional_items',
            'fixed_fee_items'
        ]

