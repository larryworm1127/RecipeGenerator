"""
Test module for util.py module

@date: 5/28/2018
@author: Larry Shi
"""

# general import
import unittest

from recipes.util import verify_data, STATE


class TestUtil(unittest.TestCase):
    def setUp(self):
        # TRUE CASES
        # Shaped Recipes
        # item and block input verify
        self.true_case1 = verify_data("Shaped", 'mod:item',
                                      ["item", "item", "item", "item", "item", "item", "item", "item", "item"],
                                      [], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [], ["ABC", "DEF", "GHI"])

        self.true_case2 = verify_data("Shaped", "mod:item", [],
                                      ["block", "block", "block", "block", "block", "block", "block", "block", "block"],
                                      [], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], ["ABC", "DEF", "GHI"])

        self.true_case3 = verify_data("Shaped", 'mod:item',
                                      ["item", "item", "item", "item", "item"], ["block", "block", "block", "block"],
                                      ['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I'], ["ABC", "DEF", "GHI"])

        self.true_case9 = verify_data("Shaped", 'mod:item', ["item_one", "item_two"], [], ['A', 'B'], [],
                                      [" A ", " A ", " B "])

        self.true_case10 = verify_data("Shaped", 'mod:item', ["item_one", "item_two"], [], ['A', 'B'], [],
                                       ["A  ", "A  ", "B  "])

        # pattern
        self.true_case4 = verify_data("Shaped", 'mod:item', ["item"], [], ['A'], [], ["AA", "AA", ""])
        self.true_case5 = verify_data("Shaped", 'mod:item', ["item"], [], ['A'], [], ["A", "", ""])

        # Shapeless Recipes
        self.true_case6 = verify_data("Shapeless", "mod:item", ["mod:item_one", "mod:item_two"], [])
        self.true_case7 = verify_data("Shapeless", "mod:item", [], ["mod:block_one", "mod:block_two"])
        self.true_case8 = verify_data("Shapeless", "mod:item", ["mod:item"], ["mod:block"])

        # FALSE CASES
        # Shaped Recipe
        # item and block input verify
        self.false_case1 = verify_data("Shaped", 'mod:item', [], [], [], [], ["ABC", "DEF", "GHI"])

        self.false_case2 = verify_data("Shaped", 'mod:item',
                                       ["item", "item", "item", "item", "item", "item", "item", "item", "item"], [],
                                       ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'], [], ["ABC", "DEF", "GHI"])

        self.false_case3 = verify_data("Shaped", 'mod:item', {},
                                       ["block", "block", "block", "block", "block", "block", "block", "block",
                                        "block"], [], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'],
                                       ["ABC", "DEF", "GHI"])

        # output verify
        self.false_case4 = verify_data("Shaped", '', ["item"], [], ['#'], [], ["###", "###", "###"])
        self.false_case5 = verify_data("Shapeless", '', ["mod:item"], [])
        self.false_case6 = verify_data("Shaped", 'item', ["item"], [], ['#'], [], ["###", "###", "###"])
        self.false_case7 = verify_data("Shapeless", 'item', ["mod:item"], [])

        # pattern verify
        self.false_case8 = verify_data("Shaped", 'mod:item', [], [], [], [], ["", "", ""])

        # Shapeless Recipe
        self.false_case9 = verify_data("Shapeless", "mod:item", [], [])

    def test_verify_data(self):
        # TRUE CASES
        # state
        self.assertEqual("PASS", STATE[self.true_case1[0]], self.true_case1[1])
        self.assertEqual("PASS", STATE[self.true_case2[0]], self.true_case2[1])
        self.assertEqual("PASS", STATE[self.true_case3[0]], self.true_case3[1])
        self.assertEqual("PASS", STATE[self.true_case4[0]], self.true_case4[1])
        self.assertEqual("PASS", STATE[self.true_case5[0]], self.true_case5[1])
        self.assertEqual("PASS", STATE[self.true_case6[0]], self.true_case6[1])
        self.assertEqual("PASS", STATE[self.true_case7[0]], self.true_case7[1])
        self.assertEqual("PASS", STATE[self.true_case8[0]], self.true_case8[1])
        self.assertEqual("PASS", STATE[self.true_case9[0]], self.true_case9[1])
        self.assertEqual("PASS", STATE[self.true_case10[0]], self.true_case10[1])

        # FALSE CASES
        # state
        self.assertEqual("FAIL", STATE[self.false_case1[0]])
        self.assertEqual("FAIL", STATE[self.false_case2[0]])
        self.assertEqual("FAIL", STATE[self.false_case3[0]])
        self.assertEqual("FAIL", STATE[self.false_case4[0]])
        self.assertEqual("FAIL", STATE[self.false_case5[0]])
        self.assertEqual("FAIL", STATE[self.false_case6[0]])
        self.assertEqual("FAIL", STATE[self.false_case7[0]])
        self.assertEqual("FAIL", STATE[self.false_case8[0]])
        self.assertEqual("FAIL", STATE[self.false_case9[0]])

        # message
        self.assertEqual("Number of keys doesn't match pattern.", self.false_case1[1])
        self.assertEqual("Item key not in pattern.", self.false_case2[1])
        self.assertEqual("Block key not in pattern.", self.false_case3[1])
        self.assertEqual("Output is empty.", self.false_case4[1])
        self.assertEqual("Output is empty.", self.false_case5[1])
        self.assertEqual("Incorrect output format.", self.false_case6[1])
        self.assertEqual("Incorrect output format.", self.false_case7[1])
        self.assertEqual("Pattern is empty.", self.false_case8[1])
        self.assertEqual("Both item input and block input are empty.", self.false_case9[1])


if __name__ == "__main__":
    unittest.main()
