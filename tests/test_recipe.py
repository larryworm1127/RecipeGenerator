"""
Test module for recipe.py modules

@date: 5/16/2018
@author: Larry Shi
"""

# general imports
import unittest

from recipes import ShapedRecipe, ShapelessRecipe


class TestShapedRecipe(unittest.TestCase):
    def setUp(self):
        self.shaped_item = ShapedRecipe("item_test", "mod:item_test",
                                        {'A': "mod:item_test"},
                                        None,
                                        [" A ", " A ", " A "])
        self.shaped_block = ShapedRecipe("item_test", "mod:item_test",
                                         None,
                                         {'A': "mod:block_test"},
                                         [" A ", " A ", " A "])

    def test_init(self):
        self.assertEqual(self.shaped_item.get_name(), "item_test", "Name doesn't match.")
        self.assertEqual(self.shaped_item.get_output(), 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shaped_item.get_count(), 1, "Output count doesn't match.")
        self.assertEqual(self.shaped_item.get_item_input(), {'A': 'mod:item_test'}, "Item input doesn't match.")
        self.assertEqual(self.shaped_item.get_block_input(), None, "Block input doesn't match.")
        self.assertEqual(self.shaped_item.get_pattern(), [' A ', ' A ', ' A '], "Pattern doesn't match.")
        self.assertEqual(self.shaped_item.get_type(), "crafting_shaped", "Type doesn't match.")

        self.assertEqual(self.shaped_block.get_name(), "item_test", "Name doesn't match.")
        self.assertEqual(self.shaped_block.get_output(), 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shaped_block.get_count(), 1, "Output count doesn't match.")
        self.assertEqual(self.shaped_block.get_item_input(), None, "Item input doesn't match.")
        self.assertEqual(self.shaped_block.get_block_input(), {'A': 'mod:block_test'}, "Block input doesn't match.")
        self.assertEqual(self.shaped_block.get_pattern(), [' A ', ' A ', ' A '], "Pattern doesn't match.")
        self.assertEqual(self.shaped_block.get_type(), "crafting_shaped", "Type doesn't match.")


class TestShapelessRecipe(unittest.TestCase):
    def setUp(self):
        self.shapeless_item = ShapelessRecipe("item_test", "mod:item_test",
                                              ["mod:item", "mod:item"],
                                              None)
        self.shapeless_block = ShapelessRecipe("item_test", "mod:item_test",
                                               None,
                                               ["mod:block", "mod:block"])

    def test_init(self):
        self.assertEqual(self.shapeless_item.get_name(), "item_test", "Name doesn't match.")
        self.assertEqual(self.shapeless_item.get_output(), 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shapeless_item.get_count(), 1, "Output count doesn't match.")
        self.assertEqual(self.shapeless_item.get_item_input(), ["mod:item", "mod:item"], "Item input doesn't match.")
        self.assertEqual(self.shapeless_item.get_block_input(), None, "Block input doesn't match.")
        self.assertEqual(self.shapeless_item.get_type(), "crafting_shapeless", "Type doesn't match.")

        self.assertEqual(self.shapeless_block.get_name(), "item_test", "Name doesn't match.")
        self.assertEqual(self.shapeless_block.get_output(), 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shapeless_block.get_count(), 1, "Output count doesn't match.")
        self.assertEqual(self.shapeless_block.get_item_input(), None, "Item input doesn't match.")
        self.assertEqual(self.shapeless_block.get_block_input(), ["mod:block", "mod:block"], "Block input don't match.")
        self.assertEqual(self.shapeless_block.get_type(), "crafting_shapeless", "Type doesn't match.")


if __name__ == '__main__':
    unittest.main()
