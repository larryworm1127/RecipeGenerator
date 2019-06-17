"""
Test module for json_generator.py module

@date: 5/24/2018
@author: Larry Shi
"""
import unittest
from json import load
from os.path import exists, join
from sys import path

from recipes.recipe import ShapedRecipe, ShapelessRecipe
from recipes.recipe_json import JsonRecipe

# path constant
GEN_PATH = join(path[0], 'tests', 'json_generator_folder')
RES_PATH = join(path[0], 'tests', 'json_results')


class TestJsonShaped(unittest.TestCase):
    def setUp(self):
        # Shaped Recipes
        self.item = ShapedRecipe(
            "shaped1", "mod:item_test",
            {'A': "mod:item_test"},
            {},
            [" A ", " A ", " A "],
            debug=True
        )
        self.block = ShapedRecipe(
            "shaped2", "mod:item_test",
            {},
            {'A': "mod:block_test"},
            [" A ", " A ", " A "],
            debug=True
        )
        self.item_block = ShapedRecipe(
            "shaped3", "mod:item_test",
            {'A': "mod:item_test"},
            {'B': "mod:block_test"},
            [" A ", " B ", " A "],
            debug=True
        )
        self.count_two = ShapedRecipe(
            "shaped4", "mod:item_test",
            {'A': "mod:item_test"}, {},
            [" A ", " A ", " A "], 2,
            debug=True
        )

        self.json_item = JsonRecipe(self.item)
        self.json_item.create_shaped_json()
        self.json_block = JsonRecipe(self.block)
        self.json_block.create_shaped_json()
        self.json_item_block = JsonRecipe(self.item_block)
        self.json_item_block.create_shaped_json()
        self.json_count_two = JsonRecipe(self.count_two)
        self.json_count_two.create_shaped_json()

        with open(join(RES_PATH, 'shaped_item_only.json')) as f:
            self.item_expected = load(f)
        with open(join(RES_PATH, 'shaped_block_only.json')) as f:
            self.block_expected = load(f)
        with open(join(RES_PATH, 'shaped_item_block.json')) as f:
            self.item_block_expected = load(f)
        with open(join(RES_PATH, 'shaped_count_two.json')) as f:
            self.count_two_expected = load(f)

    def test_json(self):
        """Test whether the content of the generated recipe is corrected.
        """
        message = "JSON doesn't match"

        # Shaped Recipes
        self.assertDictEqual(self.item_expected,
                             self.json_item.result, message)
        self.assertDictEqual(self.block_expected,
                             self.json_block.result, message)
        self.assertDictEqual(self.item_block_expected,
                             self.json_item_block.result, message)
        self.assertDictEqual(self.count_two_expected,
                             self.json_count_two.result, message)

    def test_generator(self):
        """Test whether JSON generator generates correct recipe file.
        """
        # Shaped Recipes
        self.json_item.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.item.name + '.json')))

        self.json_block.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.block.name + '.json')))

        self.json_item_block.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.item_block.name + '.json')))

        self.json_count_two.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.count_two.name + '.json')))


class TestJsonShapeless(unittest.TestCase):
    def setUp(self):
        # Shapeless Recipes
        self.item = ShapelessRecipe(
            "shapeless1", "mod:item_test",
            ["mod:item_test"],
            [],
            debug=True
        )
        self.block = ShapelessRecipe(
            "shapeless2", "mod:item_test",
            [],
            ["mod:block_test"],
            debug=True
        )
        self.item_block = ShapelessRecipe(
            "shapeless3", "mod:item_test",
            ["mod:item_test"],
            ["mod:block_test"],
            debug=True
        )
        self.count_two = ShapelessRecipe(
            "shapeless4",
            "mod:item_test", [],
            ["mod:block_test"], 2,
            debug=True
        )

        self.json_item = JsonRecipe(self.item)
        self.json_item.create_shapeless_json()
        self.json_block = JsonRecipe(self.block)
        self.json_block.create_shapeless_json()
        self.json_item_block = JsonRecipe(self.item_block)
        self.json_item_block.create_shapeless_json()
        self.json_count_two = JsonRecipe(self.count_two)
        self.json_count_two.create_shapeless_json()

        with open(join(RES_PATH, 'shapeless_item_only.json')) as f:
            self.item_expected = load(f)
        with open(join(RES_PATH, 'shapeless_block_only.json')) as f:
            self.block_expected = load(f)
        with open(join(RES_PATH, 'shapeless_item_block.json')) as f:
            self.item_block_expected = load(f)
        with open(join(RES_PATH, 'shapeless_count_two.json')) as f:
            self.count_two_expected = load(f)

    def test_json(self):
        """Test whether the content of the generated recipe is corrected.
        """
        message = "JSON doesn't match"

        # Shapeless Recipes
        self.assertDictEqual(self.item_expected,
                             self.json_item.result, message)
        self.assertDictEqual(self.block_expected,
                             self.json_block.result, message)
        self.assertDictEqual(self.item_block_expected,
                             self.json_item_block.result, message)
        self.assertDictEqual(self.count_two_expected,
                             self.json_count_two.result, message)

    def test_generator(self):
        """Test whether JSON generator generates correct recipe file.
        """
        # Shapeless Recipes
        self.json_item.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.item.name + '.json')))

        self.json_block.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.block.name + '.json')))

        self.json_item_block.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.item_block.name + '.json')))

        self.json_count_two.generator(GEN_PATH)
        self.assertTrue(exists(join(GEN_PATH, self.count_two.name + '.json')))


if __name__ == '__main__':
    unittest.main()
