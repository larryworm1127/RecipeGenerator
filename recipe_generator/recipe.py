"""
This module contains two classes for two different
types of crafting recipes: Shaped and Shapeless

May 16, 2018
Larry Shi
"""


class ShapelessRecipe:

    def __init__(self, name, output, item_input, block_input, count=1):
        self.name = name
        self.output = output
        self.output_count = count
        self.item_input = item_input
        self.block_input = block_input
        self.type = "crafting_shapeless"

    def __str__(self):
        return "Name: %s\nOutput: %s\nItem Input: %s\nBlock Input: %s\nOutput Count: %s\nType: %s\n" % (
            self.name, self.output, self.item_input, self.block_input, self.output_count, self.type)

    def get_name(self):
        return self.name

    def get_item_input(self):
        return self.item_input

    def get_output(self):
        return self.output

    def get_count(self):
        return self.output_count

    def get_block_input(self):
        return self.block_input

    def get_type(self):
        return self.type


class ShapedRecipe:

    def __init__(self, name, output, item_input, block_input, pattern, count=1):
        self.name = name
        self.output = output
        self.item_input = item_input
        self.block_input = block_input
        self.output_count = count
        self.pattern = pattern
        self.type = "crafting_shaped"

    def __str__(self):
        return "Name: %s\nOutput: %s\nItem Input: %s\nBlock Input: %s\nOutput Count: %s\nPattern: %s\nType: %s\n" % (
            self.name, self.output, self.item_input, self.block_input, self.output_count, self.pattern, self.type)

    def get_name(self):
        return self.name

    def get_output(self):
        return self.output

    def get_item_input(self):
        return self.item_input

    def get_block_input(self):
        return self.block_input

    def get_count(self):
        return self.output_count

    def get_pattern(self):
        return self.pattern

    def get_type(self):
        return self.type
