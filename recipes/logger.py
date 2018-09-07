"""
Python module that initialize a python logger

@date: 6/9/2018
@author: Larry Shi
"""

# general imports
import logging
import sys

from logging.handlers import TimedRotatingFileHandler
from os.path import join, exists
from os import mkdir

__all__ = ["get_logger"]


# logger initialization
def get_logger(name: str, debug: bool = False) -> logging.Logger:
    """
    A util function that creates a logging object and return it to the caller

    :param debug: optional parameter to avoid file path error when running tests
    :param name: the name of the logger
    :return: a logger object
    """

    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # don't create stream handler or file handler if debug is true
    if not debug:
        # create log file folder
        log_path = join(sys.path[0], 'logs')
        if not exists(log_path):
            mkdir(log_path)

        # create formatter
        file_formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        file_formatter.datefmt = '%m-%d %H:%M'
        console_formatter = logging.Formatter('%(name)-16s: %(levelname)-7s - %(message)s')

        # create file handler and set level to debug
        file_handler = TimedRotatingFileHandler(join("logs", "latest_logs.log"), when='m', interval=1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # create console handler and set level to debug
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    # return logger object
    return logger
