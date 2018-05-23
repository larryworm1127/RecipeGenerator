"""
This module contains two classes for two different
types of crafting recipes: Shaped and Shapeless

May 16, 2018
Larry Shi
"""


class ShapelessRecipe:

    def __init__(self, name, output, item_input, block_input, count):
        self._name = name
        self._output = output
        self._output_count = count
        self._item_input = item_input
        self._block_input = block_input
        self._type = "crafting_shapeless"

    def __str__(self):
        return "Name: %s\nOutput: %s\nItem Input: %s\nBlock Input: %s\nOutput Count: %s\nType: %s\n" % (
            self._name, self._output, self._item_input, self._block_input, self._output_count, self._type)

    def get_name(self):
        return self._name

    def get_item_input(self):
        return self._item_input

    def get_output(self):
        return self._output

    def get_count(self):
        return self._output_count

    def get_block_input(self):
        return self._block_input

    def get_type(self):
        return self._type


class ShapedRecipe:

    def __init__(self, name, output, item_input, block_input, count, pattern):
        self._name = name
        self._output = output
        self._item_input = item_input
        self._block_input = block_input
        self._output_count = count
        self._pattern = pattern
        self._type = "crafting_shaped"

    def __str__(self):
        return "Name: %s\nOutput: %s\nItem Input: %s\nBlock Input: %s\nOutput Count: %s\nPattern: %s\nType: %s\n" % (
            self._name, self._output, self._item_input, self._block_input, self._output_count, self._pattern,
            self._type)

    def get_name(self):
        return self._name

    def get_output(self):
        return self._output

    def get_item_input(self):
        return self._item_input

    def get_block_input(self):
        return self._block_input

    def get_count(self):
        return self._output_count

    def get_pattern(self):
        return self._pattern

    def get_type(self):
        return self._type
