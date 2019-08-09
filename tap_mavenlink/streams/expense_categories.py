from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa


class ExpenseCategoriesStream(BaseStream):
    NAME = 'ExpenseCategoriesStream'
    API_METHOD = 'GET'
    TABLE = 'expense_categories'
    KEY_PROPERTIES = ['id']

    @property
    def path(self):
        return '/expense_categories.json'

    @property
    def response_key(self):
        return 'expense_categories'
