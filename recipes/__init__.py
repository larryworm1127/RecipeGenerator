"""This package contains module for recipe creation
"""
import logging
import sys
from os import mkdir
from os.path import join, exists

__author__ = "Larry Shi"
__all__ = ["get_logger"]


# logger initialization
def get_logger(name: str, debug: bool = False) -> logging.Logger:
    """Creates a logging object and return it to the caller

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
        log_format = '%(asctime)s %(levelname)s %(message)s'
        date_format = '%Y/%m/%d %I:%M:%S'

        file_handler = logging.FileHandler(join("logs", "latest_logs.log"))
        logger.addHandler(file_handler)

        formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
        file_handler.setFormatter(formatter)

    # return logger object
    return logger
