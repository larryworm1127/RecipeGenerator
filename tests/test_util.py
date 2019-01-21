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
        self.tcase1 = verify_data(
            "Shaped", 'mod:item',
            ["i", "i", "i", "i", "i", "i", "i", "i", "i"],
            [],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            [],
            ["ABC", "DEF", "GHI"]
        )

        self.tcase2 = verify_data(
            "Shaped", "mod:item",
            [],
            ["b", "b", "b", "b", "b", "b", "b", "b", "b"],
            [],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
            ["ABC", "DEF", "GHI"]
        )

        self.tcase3 = verify_data(
            "Shaped", 'mod:item',
            ["i", "i", "i", "i", "i"],
            ["b", "b", "b", "b"],
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I'],
            ["ABC", "DEF", "GHI"]
        )

        self.tcase9 = verify_data(
            "Shaped", 'mod:item',
            ["item_one", "item_two"],
            [],
            ['A', 'B'],
            [],
            [" A ", " A ", " B "]
        )

        self.tcase10 = verify_data(
            "Shaped", 'mod:item',
            ["item_one", "item_two"],
            [],
            ['A', 'B'],
            [],
            ["A  ", "A  ", "B  "]
        )

        # pattern
        self.tcase4 = verify_data("Shaped", 'mod:i', ["i"], [], ['A'], [],
                                  ["AA", "AA", ""])
        self.tcase5 = verify_data("Shaped", 'mod:i', ["i"], [], ['A'], [],
                                  ["A", "", ""])

        # Shapeless Recipes
        self.tcase6 = verify_data("Shapeless", "mod:i",
                                  ["mod:i1", "mod:i2"], [])
        self.tcase7 = verify_data("Shapeless", "mod:i", [],
                                  ["mod:b1", "mod:b2"])
        self.tcase8 = verify_data("Shapeless", "mod:i", ["mod:i"], ["mod:b"])

        # FALSE CASES
        # Shaped Recipe
        # item and block input verify
        self.fcase1 = verify_data(
            "Shaped", 'mod:item',
            [], [], [], [],
            ["ABC", "DEF", "GHI"]
        )

        self.fcase2 = verify_data(
            "Shaped", 'mod:item',
            ["i", "i", "i", "i", "i", "i", "i", "i", "i"],
            [],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'],
            [],
            ["ABC", "DEF", "GHI"]
        )

        self.fcase3 = verify_data(
            "Shaped", 'mod:item', [],
            ["b", "b", "b", "b", "b", "b", "b", "b", "b"],
            [],
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J'],
            ["ABC", "DEF", "GHI"]
        )

        # output verify
        self.fcase4 = verify_data("Shaped", '', ["i"], [], ['#'], [],
                                  ["###", "###", "###"])
        self.fcase5 = verify_data("Shapeless", '', ["mod:item"], [])
        self.fcase6 = verify_data("Shaped", 'item', ["i"], [], ['#'],
                                  [], ["###", "###", "###"])
        self.fcase7 = verify_data("Shapeless", 'item', ["mod:item"], [])

        # pattern verify
        self.fcase8 = verify_data("Shaped", 'mod:item', [], [], [], [],
                                  ["", "", ""])

        # Shapeless Recipe
        self.fcase9 = verify_data("Shapeless", "mod:item", [], [])

    def test_verify_data_true(self):
        # TRUE CASES
        # state
        self.assertEqual("PASS", STATE[self.tcase1[0]], self.tcase1[1])
        self.assertEqual("PASS", STATE[self.tcase2[0]], self.tcase2[1])
        self.assertEqual("PASS", STATE[self.tcase3[0]], self.tcase3[1])
        self.assertEqual("PASS", STATE[self.tcase4[0]], self.tcase4[1])
        self.assertEqual("PASS", STATE[self.tcase5[0]], self.tcase5[1])
        self.assertEqual("PASS", STATE[self.tcase6[0]], self.tcase6[1])
        self.assertEqual("PASS", STATE[self.tcase7[0]], self.tcase7[1])
        self.assertEqual("PASS", STATE[self.tcase8[0]], self.tcase8[1])
        self.assertEqual("PASS", STATE[self.tcase9[0]], self.tcase9[1])
        self.assertEqual("PASS", STATE[self.tcase10[0]], self.tcase10[1])

    def test_verify_data_false(self):
        # FALSE CASES
        # state
        self.assertEqual("FAIL", STATE[self.fcase1[0]])
        self.assertEqual("FAIL", STATE[self.fcase2[0]])
        self.assertEqual("FAIL", STATE[self.fcase3[0]])
        self.assertEqual("FAIL", STATE[self.fcase4[0]])
        self.assertEqual("FAIL", STATE[self.fcase5[0]])
        self.assertEqual("FAIL", STATE[self.fcase6[0]])
        self.assertEqual("FAIL", STATE[self.fcase7[0]])
        self.assertEqual("FAIL", STATE[self.fcase8[0]])
        self.assertEqual("FAIL", STATE[self.fcase9[0]])

        # message
        self.assertEqual("# of keys don't match pattern.", self.fcase1[1])
        self.assertEqual("Item key not in pattern.", self.fcase2[1])
        self.assertEqual("Block key not in pattern.", self.fcase3[1])
        self.assertEqual("Output is empty.", self.fcase4[1])
        self.assertEqual("Output is empty.", self.fcase5[1])
        self.assertEqual("Incorrect output format.", self.fcase6[1])
        self.assertEqual("Incorrect output format.", self.fcase7[1])
        self.assertEqual("Pattern is empty.", self.fcase8[1])
        self.assertEqual("Item and block input are empty.", self.fcase9[1])


if __name__ == "__main__":
    unittest.main()
