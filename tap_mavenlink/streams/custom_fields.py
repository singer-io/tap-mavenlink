from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class CustomFieldsStream(BaseStream):
    NAME = 'CustomFieldsStream'
    API_METHOD = 'GET'
    TABLE = 'custom_fields'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/custom_fields.json'

    @property
    def response_key(self):
        return 'custom_fields'
