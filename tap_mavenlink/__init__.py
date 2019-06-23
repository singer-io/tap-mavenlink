#!/usr/bin/env python3

import singer

import tap_framework

from tap_mavenlink.client import MavenlinkClient
from tap_mavenlink.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class MavenlinkRunner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=['token'])
    client = MavenlinkClient(args.config)
    runner = MavenlinkRunner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
