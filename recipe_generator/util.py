"""
Python module that contains utility functions

Created on May 28, 2018
@author: Larry Shi
"""

# general imports
from recipe_generator.json_generator import Json
from recipe_generator.recipe import ShapedRecipe, ShapelessRecipe

# constants
STATE = {0: "PASS",
         1: "WARNING",
         2: "FAIL"}


# util functions
def verify_data(recipe_type, output, items, blocks, item_keys=None, block_keys=None, pattern=None):
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


def create_shaped_json_object(name, output, output_count, items, blocks, item_key, block_key, pattern):
    item_input = {key: item for key, item in zip(item_key, items)}
    block_input = {key: block for key, block in zip(block_key, blocks)}

    # create json object
    recipe_object = ShapedRecipe(name, output, item_input, block_input, pattern, output_count)
    json_object = Json(recipe_object)

    # return json object for other uses
    return json_object


def create_shapeless_json_object(output, output_count, items, blocks):
    # TODO move shapeless json object creation here
    pass
