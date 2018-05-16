"""
This module will be generate a JSON file for recipe created by the user

May 15, 2018
By Larry Shi
"""

# general imports
from json import dump
from os.path import join, expanduser

# constants
RECIPE_PATH = expanduser('~')


class Json:

    def __init__(self, recipe):
        self._recipe = recipe
        self._result = {}

        self.json_data()

    def __str__(self):
        return str(self._result)

    def json_data(self):
        self._result["type"] = self._recipe.get_type()
        self._result["pattern"] = self._recipe.get_pattern()

        self._result["key"] = {}
        item_input = self._recipe.get_item_input()
        if item_input is not None:
            for key, value in item_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["item"] = value

        block_input = self._recipe.get_block_input()
        if block_input is not None:
            for key, value in block_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["block"] = value

        output = self._recipe.get_output()
        self._result["result"] = {}
        self._result["result"][output[0]] = output[1]


def generator(recipe):
    result = {}

    output = recipe.get_output()
    ingredient = recipe.get_ingredient()
    recipe_type = recipe.get_type()

    if recipe_type == "shapeless":
        pass
