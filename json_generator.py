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
        self._name = recipe.get_name()
        self._result = {}

        if recipe.get_type() == "minecraft:crafting_shaped":
            self.create_shaped_json()
        else:
            self.create_shapeless_json()

    def __str__(self):
        return str(self._result)

    def get_json(self):
        return self._result

    def get_name(self):
        return self._name

    def create_shaped_json(self):
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

    def create_shapeless_json(self):
        self._result["type"] = self._recipe.get_type()

        self._result["ingredients"] = []
        item_input = self._recipe.get_item_input()
        if item_input is not None:
            for value in item_input:
                self._result["ingredients"].append({"item": value})

        block_input = self._recipe.get_block_input()
        if block_input is not None:
            for value in block_input:
                self._result["ingredients"].append({"item": value})

        output = self._recipe.get_output()
        self._result["result"] = {}
        self._result["result"][output[0]] = output[1]


def generator(recipe_json):
    path = join(RECIPE_PATH, recipe_json.get_name() + '.json')
    with open(path, 'w') as outfile:
        dump(recipe_json.get_json(), outfile)
