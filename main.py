#!/usr/bin/python
from lib.logger import Logger
from lib.storage import Storage
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

if __name__ == "__main__":
    store = Storage()
    logger = Logger(store)

    logger.run()


