from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class InvoicesStream(BaseStream):
    NAME = 'InvoicesStream'
    API_METHOD = 'GET'
    TABLE = 'invoices'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/invoices.json'

    @property
    def response_key(self):
        return 'invoices'
