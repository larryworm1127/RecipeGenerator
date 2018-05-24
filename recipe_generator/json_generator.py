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
        self._name = self._recipe.get_name()
        self._type = self._recipe.get_type()

        if self._type == "crafting_shaped":
            self._result = {"type": self._type,
                            "pattern": [],
                            "key": {},
                            "result": {}}
            self.create_shaped_json()
        else:
            self._result = {"type": self._type,
                            "ingredients": [],
                            "result": {}}
            self.create_shapeless_json()

    def __str__(self):
        return self._result

    def get_json(self):
        return self._result

    def get_name(self):
        return self._name

    def create_shaped_json(self):
        self._result["pattern"] = self._recipe.get_pattern()

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
        self._result["result"][output[0]] = output[1]
        self._result["result"]["count"] = self._recipe.get_count()

    def create_shapeless_json(self):
        item_input = self._recipe.get_item_input()
        if item_input is not None:
            for value in item_input:
                self._result["ingredients"].append({"item": value})

        block_input = self._recipe.get_block_input()
        if block_input is not None:
            for value in block_input:
                self._result["ingredients"].append({"item": value})

        output = self._recipe.get_output()
        self._result["result"][output[0]] = output[1]

    def generator(self):
        path = join(RECIPE_PATH, self._name + '.json')
        with open(path, 'w') as outfile:
            dump(self.get_json(), outfile)
