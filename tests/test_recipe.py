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
        self.shaped_item = ShapedRecipe("item_test", "mod:item_test", {'A': "mod:item_test"},
                                        None, [" A ", " A ", " A "], debug=True)
        self.shaped_block = ShapedRecipe("item_test", "mod:item_test",
                                         None, {'A': "mod:block_test"}, [" A ", " A ", " A "], debug=True)

    def test_init(self):
        self.assertEqual(self.shaped_item.name, "item_test", "Name doesn't match.")
        self.assertEqual(self.shaped_item.output, 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shaped_item.output_count, 1, "Output count doesn't match.")
        self.assertEqual(self.shaped_item.item_input, {'A': 'mod:item_test'}, "Item input doesn't match.")
        self.assertEqual(self.shaped_item.block_input, None, "Block input doesn't match.")
        self.assertEqual(self.shaped_item.pattern, [' A ', ' A ', ' A '], "Pattern doesn't match.")
        self.assertEqual(self.shaped_item.type, "crafting_shaped", "Type doesn't match.")

        self.assertEqual(self.shaped_block.name, "item_test", "Name doesn't match.")
        self.assertEqual(self.shaped_block.output, 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shaped_block.output_count, 1, "Output count doesn't match.")
        self.assertEqual(self.shaped_block.item_input, None, "Item input doesn't match.")
        self.assertEqual(self.shaped_block.block_input, {'A': 'mod:block_test'}, "Block input doesn't match.")
        self.assertEqual(self.shaped_block.pattern, [' A ', ' A ', ' A '], "Pattern doesn't match.")
        self.assertEqual(self.shaped_block.type, "crafting_shaped", "Type doesn't match.")


class TestShapelessRecipe(unittest.TestCase):
    def setUp(self):
        self.shapeless_item = ShapelessRecipe("item_test", "mod:item_test", ["mod:item", "mod:item"], None, debug=True)
        self.shapeless_block = ShapelessRecipe("item_test", "mod:item_test", None, ["mod:block", "mod:block"], debug=True)

    def test_init(self):
        self.assertEqual(self.shapeless_item.name, "item_test", "Name doesn't match.")
        self.assertEqual(self.shapeless_item.output, 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shapeless_item.output_count, 1, "Output count doesn't match.")
        self.assertEqual(self.shapeless_item.item_input, ["mod:item", "mod:item"], "Item input doesn't match.")
        self.assertEqual(self.shapeless_item.block_input, None, "Block input doesn't match.")
        self.assertEqual(self.shapeless_item.type, "crafting_shapeless", "Type doesn't match.")

        self.assertEqual(self.shapeless_block.name, "item_test", "Name doesn't match.")
        self.assertEqual(self.shapeless_block.output, 'mod:item_test', "Output doesn't match.")
        self.assertEqual(self.shapeless_block.output_count, 1, "Output count doesn't match.")
        self.assertEqual(self.shapeless_block.item_input, None, "Item input doesn't match.")
        self.assertEqual(self.shapeless_block.block_input, ["mod:block", "mod:block"], "Block input don't match.")
        self.assertEqual(self.shapeless_block.type, "crafting_shapeless", "Type doesn't match.")


if __name__ == '__main__':
    unittest.main()
