"""
Testing module for other modules and classes

May 16, 2018
Larry Shi
"""

# general imports
from unittest import TestCase
from os.path import exists
from json import load

from json_generator import generator, RECIPE_PATH
from tests.cases import *


class TestShapedRecipe(TestCase):
    def test_str(self):
        self.assertEqual(test_shaped_item_only.__str__(), result_shaped_item_only, "String doesn't match.")
        self.assertEqual(test_shaped_block_only.__str__(), result_shaped_block_only, "String doesn't match.")


class TestShapelessRecipe(TestCase):
    def test_str(self):
        self.assertTrue(recipe_three)
        self.assertTrue(recipe_four)


class TestJson(TestCase):
    def test_str(self):
        with open(shaped_item_only_json_path) as shaped_item_only_file:
            expected = load(shaped_item_only_file)
            self.assertDictEqual(json_shaped_item_only.get_json(), expected, "JSON doesn't match.")
        with open(shaped_block_only_json_path) as shaped_block_only_file:
            expected = load(shaped_block_only_file)
            self.assertDictEqual(json_shaped_block_only.get_json(), expected, "JSON doesn't match.")

    def test_generator(self):
        json_one = Json(test_shaped_item_only)
        generator(json_one)
        self.assertTrue(exists(join(RECIPE_PATH, json_one.get_name() + '.json')))

        json_two = Json(test_shaped_block_only)
        generator(json_two)
        self.assertTrue(exists(join(RECIPE_PATH, json_two.get_name() + '.json')))
