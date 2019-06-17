"""
Python module that generates a JSON file for recipe created by the user

@date: 5/14/2018
@author: Larry Shi
"""

# general imports
from json import dump, dumps
from os.path import join, expanduser, exists
from typing import Union

from . import get_logger
from .recipe import ShapelessRecipe, ShapedRecipe

__all__ = ["JsonRecipe"]

# constants
RECIPE_PATH = expanduser('~')


# json class
class JsonRecipe:
    """Class for recipe json object"""

    def __init__(self, recipe: Union[ShapedRecipe, ShapelessRecipe]):
        # initialize variables
        self.recipe = recipe
        self.name = recipe.name
        self.type = recipe.type
        self._logger = get_logger("recipe_json.Json", recipe.debug)

        # actions for shaped recipe
        if self.type == "crafting_shaped":
            self.result = {"type": f"minecraft: {self.type}", "pattern": [],
                           "key": {}, "result": {}}
            self.create_shaped_json()

        # actions for shapeless recipe
        else:
            self.result = {"type": f"minecraft: {self.type}",
                           "ingredients": [], "result": {}}
            self.create_shapeless_json()

    def __str__(self) -> str:
        self._logger.info("Create string representation of JSON recipe")
        return dumps(self.result, indent=2)

    def create_shaped_json(self) -> None:
        """Creates a shaped recipe json using given recipe class.
        """
        self._logger.info("Create shaped JSON recipe")

        # pattern
        self.result["pattern"] = self.recipe.pattern

        # item ingredients
        item_input = self.recipe.item_input
        if item_input is not None:
            for key, value in item_input.items():
                self.result["key"][key] = {}
                self.result["key"][key]["item"] = value

        # block ingredients
        block_input = self.recipe.block_input
        if block_input is not None:
            for key, value in block_input.items():
                self.result["key"][key] = {}
                self.result["key"][key]["block"] = value

        # recipe output
        output = self.recipe.output
        self.result["result"]["item"] = output
        self.result["result"]["count"] = int(self.recipe.output_count)

    def create_shapeless_json(self) -> None:
        """Creates a shapeless recipe json using given recipe class.
        """
        self._logger.info("Create shapeless JSON recipe")

        # item ingredients
        item_input = self.recipe.item_input
        if item_input is not None:
            for value in item_input:
                self.result["ingredients"].append({"item": value})

        # block ingredients
        block_input = self.recipe.block_input
        if block_input is not None:
            for value in block_input:
                self.result["ingredients"].append({"block": value})

        # recipe output
        output = self.recipe.output
        self.result["result"]["item"] = output
        self.result["result"]["count"] = int(self.recipe.output_count)

    def generator(self, base_path: str) -> bool:
        """Creates the json file from the given dir path.

        :param base_path: the path of the directory
        :return: boolean of whether the file creation was successful
        """
        self._logger.info("Create JSON recipe file at given file location")

        path = join(base_path, self.name + '.json')
        with open(path, 'w') as outfile:
            dump(self.result, outfile)

        if exists(path):
            return True
        else:
            self._logger.error("File creation failed")
            return False
