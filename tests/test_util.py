"""
Test module for util.py module

Created on May 28, 2018
@author: Larry Shi
"""

# general import
import unittest

from recipe_generator.util import verify_data


class TestUtil(unittest.TestCase):
    def setUp(self):
        # TRUE CASES
        # Shaped Recipes
        # item and block input verify
        self.true_case1 = verify_data("Shaped", 'item',
                                      {'A': "item", 'B': "item", 'C': "item", 'D': "item", 'E': "item", 'F': "item",
                                       'G': "item", 'H': "item", 'I': "item"}, {},
                                      ["ABC", "DEF", "GHI"])

        self.true_case2 = verify_data("Shaped", "item", {},
                                      {'A': "block", 'B': "block", 'C': "block", 'D': "block", 'E': "block",
                                       'F': "block", 'G': "block", 'H': "block", 'I': "block"},
                                      ["ABC", "DEF", "GHI"])

        self.true_case3 = verify_data("Shaped", 'item',
                                      {'A': "item", 'B': "item", 'C': "item", 'D': "item", 'E': "item"},
                                      {'F': "block", 'G': "block", 'H': "block", 'I': "block"},
                                      ["ABC", "DEF", "GHI"])

        # Shapeless Recipes
        self.true_case4 = verify_data("Shapeless", "item", ["mod:item_one", "mod:item_two"], [])
        self.true_case5 = verify_data("Shapeless", "item", [], ["mod:block_one", "mod:block_two"])
        self.true_case6 = verify_data("Shapeless", "item", ["mod:item"], ["mod:block"])

        # FALSE CASES
        # Shaped Recipe
        # item and block input verify
        self.false_case1 = verify_data("Shaped", 'item', {}, {}, ["ABC", "DEF", "GHI"])

        self.false_case2 = verify_data("Shaped", 'item',
                                       {'A': "item", 'B': "item", 'C': "item", 'D': "item", 'E': "item", 'F': "item",
                                        'G': "item", 'H': "item", 'J': "item"}, {},
                                       ["ABC", "DEF", "GHI"])

        self.false_case3 = verify_data("Shaped", 'item', {},
                                       {'A': "block", 'B': "block", 'C': "block", 'D': "block", 'E': "block",
                                        'F': "block", 'G': "block", 'H': "block", 'J': "block"},
                                       ["ABC", "DEF", "GHI"])

        self.false_case4 = verify_data("Shaped", 'item',
                                       {'A': "item", 'B': "item", 'C': "item", 'D': "item", 'Z': "item"},
                                       {'F': "block", 'G': "block", 'H': "block", 'J': "block"},
                                       ["ABC", "DEF", "GHI"])

        # output verify
        self.false_case5 = verify_data("Shaped", '', {'#': "item"}, {}, ["###", "###", "###"])
        self.false_case6 = verify_data("Shapeless", '', ["mod:item"], [])

        # pattern verify
        self.false_case7 = verify_data("Shaped", 'item', {}, {}, ["", "", ""])

        # Shapeless Recipe
        self.false_case8 = verify_data("Shapeless", "item", [], [])

    def test_verify_data_for_json(self):
        # true cases
        self.assertTrue(self.true_case1)
        self.assertTrue(self.true_case2)
        self.assertTrue(self.true_case3)

        # false cases
        self.assertFalse(self.false_case1)
        self.assertFalse(self.false_case2)
        self.assertFalse(self.false_case3)
        self.assertFalse(self.false_case4)
        self.assertFalse(self.false_case5)
        self.assertFalse(self.false_case6)
        self.assertFalse(self.false_case7)
        self.assertFalse(self.false_case8)


if __name__ == "__main__":
    unittest.main()
