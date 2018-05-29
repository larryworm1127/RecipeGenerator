"""
Python module that contains utility functions

Created on May 28, 2018
@author: Larry Shi
"""


def verify_data(recipe_type, output, item_input, block_input, pattern=None):
    # check output
    if output == '':
        return False

    # shaped recipe
    if recipe_type == "Shaped":

        # check pattern
        if len(pattern[0]) and len(pattern[1]) and len(pattern[2]) != 0:
            keys = set([key for row in pattern for key in row])
        else:
            return False

        # check item input
        for item_key in item_input.keys():
            if item_key in keys:
                keys.remove(item_key)
            else:
                return False

        # check block input
        for block_key in block_input.keys():
            if block_key in keys:
                keys.remove(block_key)
            else:
                return False

        if len(keys) > 0:
            return False

        # default is true
        return True

    # shapeless recipe
    else:
        # check item input and block input
        if len(item_input) == 0 and len(block_input) == 0:
            return False

        # default is true
        return True
