"""
This module contains all the cases for tests as well as
path and data for expected results

May 19, 2018
Larry Shi
"""
# general imports
from os.path import join
from sys import path

from json_generator import Json
from recipe import ShapedRecipe, ShapelessRecipe

JSON_RESULT_PATH = join(path[0], 'tests', 'json_results')

"""Shaped Recipe"""
# ingredient item only
test_shaped_item_only = ShapedRecipe("item_test", ("item", "mod:item_test"),
                                     {'A': "mod:item_test"},
                                     None,
                                     1, [" A ", " A ", " A "])
json_shaped_item_only = Json(test_shaped_item_only)
result_shaped_item_only = "Name: item_test\n" \
                          "Output: ('item', 'mod:item_test')\n" \
                          "Item Input: {'A': 'mod:item_test'}\n" \
                          "Block Input: None\n" \
                          "Output Count: 1\n" \
                          "Pattern: [' A ', ' A ', ' A ']\n" \
                          "Type: crafting_shaped\n"
shaped_item_only_json_path = join(JSON_RESULT_PATH, 'shaped_item_only.json')

# ingredient block only
test_shaped_block_only = ShapedRecipe("item_test", ("item", "mod:item_test"),
                                      None,
                                      {'A': "mod:block_test"},
                                      1, [" A ", " A ", " A "])
json_shaped_block_only = Json(test_shaped_block_only)
result_shaped_block_only = "Name: item_test\n" \
                           "Output: ('item', 'mod:item_test')\n" \
                           "Item Input: None\n" \
                           "Block Input: {'A': 'mod:block_test'}\n" \
                           "Output Count: 1\n" \
                           "Pattern: [' A ', ' A ', ' A ']\n" \
                           "Type: crafting_shaped\n"
shaped_block_only_json_path = join(JSON_RESULT_PATH, 'shaped_block_only.json')

"""Shapeless Recipe"""
recipe_three = ShapelessRecipe("ingot_test_one", ("item", "mod:ingot_test_one"),
                               ["mod:ingot_test_two", "mod:ingot_test_three"],
                               None, 1)

recipe_four = ShapelessRecipe("block_test", ("block", "mod:block_test"),
                              ["mod:ingot_test_one", "mod:ingot_test_two"],
                              None, 1)
