
from tap_mavenlink.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()  # noqa

"""
# TODO : Complete me!

Implementing a custom stream:
    1. Specify the request details
        - API_METHOD: GET or POST; usually GET
        - TABLE: The Stitch destination table where this data should end up
        - KEY_PROPERTIES: The primary key (or a surrogate key of many fields)=
                          which uniquely identifies a given record

    2. Implement the helper "property" methods
        - path: Returns the path (concatenated with the "base" path from base.py) for this resource
        - response_key: Returns the key which contains the payload data in the response data
        - include: Returns a list of fields to be specified as the ?include= parameters to the query

Notes:
 - Make sure the Stream `class` name matches up with the one specified in __init__.py
 - This class _inherits_ from BaseStream (base.py)
    - If a method isn't overriden in UsersStream, then the default implementation
      for that method is taken from BaseStream
 - Trace the logic in BaseStream.sync_paginated to follow how the tap works
 - Be sure to un-comment streams in __init__.py as you add them!
"""


class UsersStream(BaseStream):
    API_METHOD = '...'
    TABLE = '...'
    KEY_PROPERTIES = ['...']

    @property
    def path(self):
        return '...'

    @property
    def response_key(self):
        return '...'

    @property
    def include(self):
        # TODO : What goes in here?
        return []
