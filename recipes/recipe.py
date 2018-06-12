"""
Python module that contains two classes for Shaped and Shapeless recipes

@date: 5/16/2018
@author: Larry Shi
"""

from recipes import util


# recipe classes
class ShapelessRecipe:

    def __init__(self, name, output, item_input, block_input, count=1, debug=False):
        # initialize variables
        self.name = name
        self.output = output
        self.output_count = count
        self.item_input = item_input
        self.block_input = block_input
        self.type = "crafting_shapeless"

        # logging
        self.debug = debug
        self.logger = util.get_logger("recipe.ShapelessRecipe", debug)
        self.logger.info("Shapeless recipe object created")

    def __str__(self):
        return "Name: {}\nOutput: {}\nItem Input: {}\nBlock Input: {}\nOutput Count: {}\nType: {}\n".format(
            self.name, self.output, self.item_input, self.block_input, self.output_count, self.type)


class ShapedRecipe:

    def __init__(self, name, output, item_input, block_input, pattern, count=1, debug=False):
        # initialize variables
        self.name = name
        self.output = output
        self.item_input = item_input
        self.block_input = block_input
        self.output_count = count
        self.pattern = pattern
        self.type = "crafting_shaped"

        # logging
        self.debug = debug
        self.logger = util.get_logger("recipe.ShapedRecipe", debug)
        self.logger.info("Shaped recipe object created")

    def __str__(self):
        return "Name: {}\nOutput: {}\nItem Input: {}\nBlock Input: {}\nOutput Count: {}\nPattern: " \
               "{}\nType: {}\n".format(self.name, self.output, self.item_input, self.block_input, self.output_count,
                                       self.pattern, self.type)
