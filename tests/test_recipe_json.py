"""
Test module for json_generator.py module

@date: 5/24/2018
@author: Larry Shi
"""

# general imports
import unittest
from os.path import exists, join
from sys import path
from json import load

from recipes import ShapedRecipe, Json, ShapelessRecipe

# path constant
JSON_GENERATOR_PATH = join(path[0], 'tests', 'json_generator_folder')
JSON_RESULT_PATH = join(path[0], 'tests', 'json_results')


class TestJson(unittest.TestCase):
    def setUp(self):
        # Shaped Recipes
        self.shaped_item = ShapedRecipe("shaped1", "mod:item_test", {'A': "mod:item_test"}, None,
                                        [" A ", " A ", " A "])
        self.shaped_block = ShapedRecipe("shaped2", "mod:item_test", None, {'A': "mod:block_test"},
                                         [" A ", " A ", " A "])
        self.shaped_item_block = ShapedRecipe("shaped3", "mod:item_test", {'A': "mod:item_test"},
                                              {'B': "mod:block_test"}, [" A ", " B ", " A "])
        self.shaped_count_two = ShapedRecipe("shaped4", "mod:item_test", {'A': "mod:item_test"}, None,
                                             [" A ", " A ", " A "], 2)

        self.json_shaped_item = Json(self.shaped_item)
        self.json_shaped_block = Json(self.shaped_block)
        self.json_shaped_item_block = Json(self.shaped_item_block)
        self.json_shaped_count_two = Json(self.shaped_count_two)

        with open(join(JSON_RESULT_PATH, 'shaped_item_only.json')) as shaped_item_file:
            self.shaped_item_expected = load(shaped_item_file)
        with open(join(JSON_RESULT_PATH, 'shaped_block_only.json')) as shaped_block_file:
            self.shaped_block_expected = load(shaped_block_file)
        with open(join(JSON_RESULT_PATH, 'shaped_item_block.json')) as shaped_item_block_file:
            self.shaped_item_block_expected = load(shaped_item_block_file)
        with open(join(JSON_RESULT_PATH, 'shaped_count_two.json')) as shaped_count_two_file:
            self.shaped_count_two_expected = load(shaped_count_two_file)

        # Shapeless Recipes
        self.shapeless_item = ShapelessRecipe("shapeless1", "mod:item_test", ["mod:item_test"], None)
        self.shapeless_block = ShapelessRecipe("shapeless2", "mod:item_test", None, ["mod:block_test"])
        self.shapeless_item_block = ShapelessRecipe("shapeless3", "mod:item_test", ["mod:item_test"], ["mod:block_test"])
        self.shapeless_count_two = ShapelessRecipe("shapeless4", "mod:item_test", None, ["mod:block_test"], 2)

        self.json_shapeless_item = Json(self.shapeless_item)
        self.json_shapeless_block = Json(self.shapeless_block)
        self.json_shapeless_item_block = Json(self.shapeless_item_block)
        self.json_shapeless_count_two = Json(self.shapeless_count_two)

        with open(join(JSON_RESULT_PATH, 'shapeless_item_only.json')) as shapeless_item_only_file:
            self.shapeless_item_expected = load(shapeless_item_only_file)
        with open(join(JSON_RESULT_PATH, 'shapeless_block_only.json')) as shapeless_block_only_file:
            self.shapeless_block_expected = load(shapeless_block_only_file)
        with open(join(JSON_RESULT_PATH, 'shapeless_item_block.json')) as shapeless_item_block_file:
            self.shapeless_item_block_expected = load(shapeless_item_block_file)
        with open(join(JSON_RESULT_PATH, 'shapeless_count_two.json')) as shapeless_count_two_file:
            self.shapeless_count_two_expected = load(shapeless_count_two_file)

    def test_json(self):
        message = "JSON doesn't match"

        # Shaped Recipes
        self.assertDictEqual(self.shaped_item_expected, self.json_shaped_item.get_json(), message)
        self.assertDictEqual(self.shaped_block_expected, self.json_shaped_block.get_json(), message)
        self.assertDictEqual(self.shaped_item_block_expected, self.json_shaped_item_block.get_json(), message)
        self.assertDictEqual(self.shaped_count_two_expected, self.json_shaped_count_two.get_json(), message)

        # Shapeless Recipes
        self.assertDictEqual(self.shapeless_item_expected, self.json_shapeless_item.get_json(), message)
        self.assertDictEqual(self.shapeless_block_expected, self.json_shapeless_block.get_json(), message)
        self.assertDictEqual(self.shapeless_item_block_expected, self.json_shapeless_item_block.get_json(), message)
        self.assertDictEqual(self.shapeless_count_two_expected, self.json_shapeless_count_two.get_json(), message)

    def test_generator(self):
        # Shaped Recipes
        self.json_shaped_item.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_item.get_name() + '.json')))

        self.json_shaped_block.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_block.get_name() + '.json')))

        self.json_shaped_item_block.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_item_block.get_name() + '.json')))

        self.json_shaped_count_two.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shaped_count_two.get_name() + '.json')))

        # Shapeless Recipes
        self.json_shapeless_item.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shapeless_item.get_name() + '.json')))

        self.json_shapeless_block.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shapeless_block.get_name() + '.json')))

        self.json_shapeless_item_block.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shapeless_item_block.get_name() + '.json')))

        self.json_shapeless_count_two.generator(JSON_GENERATOR_PATH)
        self.assertTrue(exists(join(JSON_GENERATOR_PATH, self.shapeless_count_two.get_name() + '.json')))


if __name__ == '__main__':
    unittest.main()
