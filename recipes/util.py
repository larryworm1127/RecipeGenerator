"""
Python module that contains utility functions

@date: 5/28/2018
@author: Larry Shi
"""

# general imports
import logging
from logging.handlers import TimedRotatingFileHandler
from os.path import join, exists
import sys
from os import mkdir

from .recipe_json import Json
from .recipe import ShapedRecipe, ShapelessRecipe

# constants
STATE = {0: "PASS",
         1: "WARNING",
         2: "FAIL"}

LOGGING_LEVEL = {
    1: "DEBUG",
    2: "INFO",
    3: "WARNING",
    4: "ERROR",
    5: "CRITICAL"
}


# util functions
def verify_data(recipe_type, output, items, blocks, item_keys=None, block_keys=None, pattern=None):
    """
    A util function that checks whether the user entered
    all required data and whether the data is valid or not

    :param recipe_type: the type of recipe
    :param output: the output of the recipe
    :param items: the item inputs of recipe
    :param blocks: the block inputs of recipe
    :param item_keys: the item keys used in pattern
    :param block_keys: the block keys used in pattern
    :param pattern: the pattern of shaped recipe
    :return: a integer for state and an state message
    """
    # check output
    if output == '':
        return 2, "Output is empty."

    try:
        output.split(':')[1]
    except IndexError:
        return 2, "Incorrect output format."

    # shaped recipe
    if recipe_type == "Shaped":

        # check pattern
        if len(pattern[0]) == 0 and len(pattern[1]) == 0 and len(pattern[2]) == 0:
            return 2, "Pattern is empty."
        else:
            keys = set([key for row in pattern for key in row])
            keys.discard(' ')

        # check item input
        for item_key in item_keys:
            if item_key in keys and items[item_keys.index(item_key)] != '':
                keys.remove(item_key)
            else:
                return 2, "Item key not in pattern."

        # check block input
        for block_key in block_keys:
            if block_key in keys and blocks[block_keys.index(block_key)] != '':
                keys.remove(block_key)
            else:
                return 2, "Block key not in pattern."

        if len(keys) > 0:
            return 2, "Number of keys doesn't match pattern."

        # default is pass
        return 0, "Pass"

    # shapeless recipe
    else:
        # check item input and block input
        if len(items) == 0 and len(blocks) == 0:
            return 2, "Both item input and block input are empty."

        # default is pass
        return 0, "Pass"


def create_shaped_json(name, output, output_count, items, blocks, item_key, block_key, pattern):
    """
    A util function for creating a json object for a shaped recipe

    :param name: the name of the recipe
    :param output: the output of the recipe
    :param output_count: the amount of output
    :param items: the item inputs of the recipe
    :param blocks: the block inputs of the recipe
    :param item_key: the item keys used in pattern
    :param block_key: the block keys used in pattern
    :param pattern: the pattern for shaped recipe
    :return: json object for shaped recipe
    """
    item_input = {key: item for key, item in zip(item_key, items)}
    block_input = {key: block for key, block in zip(block_key, blocks)}

    # create json object
    recipe_object = ShapedRecipe(name, output, item_input, block_input, pattern, output_count)
    json_object = Json(recipe_object)

    # return json object for other uses
    return json_object


def create_shapeless_json(name, output, output_count, items, blocks):
    """
    A util function for creating a json object for a shapeless recipe

    :param name: the name of the recipe
    :param output: the output of the recipe
    :param output_count: the amount of output
    :param items: the item inputs of the recipe
    :param blocks: the block inputs of the recipe
    :return: json object for shapeless recipe
    """
    # create json object
    recipe_object = ShapelessRecipe(name, output, items, blocks, output_count)
    json_object = Json(recipe_object)

    # return json object for other uses
    return json_object


def get_logger(name, debug=False):
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
