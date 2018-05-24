# general imports
import unittest
from os.path import exists, join
from sys import path
from json import load

from recipe_generator.json_generator import RECIPE_PATH
from recipe_generator.recipe import ShapedRecipe
from recipe_generator.json_generator import Json

JSON_RESULT_PATH = join(path[0], 'tests', 'json_results')


class TestJson(unittest.TestCase):
    def setUp(self):
        self.shaped_item = ShapedRecipe("item_test", ("item", "mod:item_test"),
                                        {'A': "mod:item_test"},
                                        None,
                                        [" A ", " A ", " A "])
        self.shaped_block = ShapedRecipe("item_test", ("item", "mod:item_test"),
                                         None,
                                         {'A': "mod:block_test"},
                                         [" A ", " A ", " A "])

        self.shaped_item_path = join(JSON_RESULT_PATH, 'shaped_item_only.json')
        self.shaped_block_path = join(JSON_RESULT_PATH, 'shaped_block_only.json')

        self.json_shaped_item = Json(self.shaped_item)
        self.json_shaped_block = Json(self.shaped_block)

    def test_str(self):
        with open(self.shaped_item_path) as shaped_item_only_file:
            expected = load(shaped_item_only_file)
            self.assertDictEqual(self.json_shaped_item.get_json(), expected, "JSON doesn't match.")

        with open(self.shaped_block_path) as shaped_block_only_file:
            expected = load(shaped_block_only_file)
            self.assertDictEqual(self.json_shaped_block.get_json(), expected, "JSON doesn't match.")

    def test_generator(self):
        self.json_shaped_item.generator()
        self.assertTrue(exists(join(RECIPE_PATH, self.shaped_item.get_name() + '.json')))

        self.json_shaped_block.generator()
        self.assertTrue(exists(join(RECIPE_PATH, self.shaped_block.get_name() + '.json')))


if __name__ == '__main__':
    unittest.main()
