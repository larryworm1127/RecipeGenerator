"""
Python module that contains utility functions

@date: 5/28/2018
@author: Larry Shi
"""
from typing import Tuple, List

from .recipe import ShapedRecipe, ShapelessRecipe
from .recipe_json import JsonRecipe

__all__ = [
    "verify_data",
    "create_shaped_json",
    "create_shapeless_json",
    "STATE"
]

# constants
STATE = {
    0: "PASS",
    1: "WARNING",
    2: "FAIL"
}

LOGGING_LEVEL = {
    1: "DEBUG",
    2: "INFO",
    3: "WARNING",
    4: "ERROR",
    5: "CRITICAL"
}


# util functions
def verify_data(recipe_type: str,
                output: str,
                items: List[str],
                blocks: List[str],
                item_keys: List[str] = None,
                block_keys: List[str] = None,
                pattern: List[str] = None) -> Tuple[int, str]:
    """Checks the validity of user input

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
        if len(pattern[0]) == 0 and len(pattern[1]) == 0 and len(
                pattern[2]) == 0:
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
            return 2, "# of keys don't match pattern."

        # default is pass
        return 0, "Pass"

    # shapeless recipe
    else:
        # check item input and block input
        if len(items) == 0 and len(blocks) == 0:
            return 2, "Item and block input are empty."

        # default is pass
        return 0, "Pass"


def create_shaped_json(name: str,
                       output: str,
                       output_count: int,
                       items: List[str],
                       blocks: List[str],
                       item_key: List[str],
                       block_key: List[str],
                       pattern: List[str]) -> JsonRecipe:
    """Creating a json object for a shaped recipe

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
    recipe_object = ShapedRecipe(name, output, item_input, block_input, pattern,
                                 output_count)
    json_object = JsonRecipe(recipe_object)
    json_object.create_shaped_json()

    # return json object for other uses
    return json_object


def create_shapeless_json(name: str,
                          output: str,
                          output_count: int,
                          items: List[str],
                          blocks: List[str]) -> JsonRecipe:
    """Creating a json object for a shapeless recipe

    :param name: the name of the recipe
    :param output: the output of the recipe
    :param output_count: the amount of output
    :param items: the item inputs of the recipe
    :param blocks: the block inputs of the recipe
    :return: json object for shapeless recipe
    """
    # create json object
    recipe_object = ShapelessRecipe(name, output, items, blocks, output_count)
    json_object = JsonRecipe(recipe_object)
    json_object.create_shapeless_json()

    # return json object for other uses
    return json_object
