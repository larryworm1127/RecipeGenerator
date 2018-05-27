"""
Test module for json_generator.py module

Created on May 24, 2018
@author: Larry Shi
"""

# general imports
import unittest
from os.path import exists, join
from sys import path
from json import load

from recipe_generator.recipe import ShapedRecipe
from recipe_generator.json_generator import Json

# path constant
JSON_GENERATOR_PATH = join(path[0], 'tests', 'json_generator_folder')
JSON_RESULT_PATH = join(path[0], 'tests', 'json_results')


class TestJson(unittest.TestCase):
    def setUp(self):
        self.shaped_item = ShapedRecipe("item_test", "mod:item_test",
                                        {'A': "mod:item_test"}, None,
                                        [" A ", " A ", " A "])
        self.shaped_block = ShapedRecipe("item_test", "mod:item_test",
                                         None, {'A': "mod:block_test"},
                                         [" A ", " A ", " A "])

        self.json_shaped_item = Json(self.shaped_item)
        self.json_shaped_block = Json(self.shaped_block)

        with open(join(JSON_RESULT_PATH, 'shaped_item_only.json')) as shaped_item_file:
            self.shaped_item_expected = load(shaped_item_file)
        with open(join(JSON_RESULT_PATH, 'shaped_block_only.json')) as shaped_block_file:
            self.shaped_block_expected = load(shaped_block_file)

    def test_json(self):
        self.assertDictEqual(self.json_shaped_item.get_json(), self.shaped_item_expected, "JSON doesn't match.")
        self.assertDictEqual(self.json_shaped_block.get_json(), self.shaped_block_expected, "JSON doesn't match.")

    def test_generator(self):
        self.json_shaped_item.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_item.get_name() + '.json')))

        self.json_shaped_block.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_block.get_name() + '.json')))


if __name__ == '__main__':
    unittest.main()
