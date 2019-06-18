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
    streams = [s for s in AVAILABLE_STREAMS if s.ENABLED]
    runner = MavenlinkRunner(
        args, client, streams)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == '__main__':
    main()
