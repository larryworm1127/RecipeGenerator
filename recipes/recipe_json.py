"""
Python module that generates a JSON file for recipe created by the user

@date: 5/14/2018
@author: Larry Shi
"""
import logging
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
    """Class for recipe json object

    === Attributes ===
    recipe:
        the recipe object to be converted to JSON.
    logger:
        the logging object for this class.
    """
    recipe: Union[ShapedRecipe, ShapelessRecipe]
    logger: logging.Logger

    def __init__(self, recipe: Union[ShapedRecipe, ShapelessRecipe]) -> None:
        # initialize variables
        self.recipe = recipe
        self.logger = get_logger("recipe_json.Json", recipe.debug)

        if self.recipe.type == "crafting_shaped":
            self.result = {
                "type": f"minecraft:{self.recipe.type}",
                "pattern": [],
                "key": {},
                "result": {}
            }
        else:
            self.result = {
                "type": f"minecraft:{self.recipe.type}",
                "ingredients": [],
                "result": {}
            }

    def __str__(self) -> str:
        """Returns human-readable JSON recipe for preview.
        """
        self.logger.info("Create string representation of JSON recipe")
        return dumps(self.result, indent=2)

    def create_shaped_json(self) -> None:
        """Creates a shaped recipe json using given recipe class.
        """
        self.logger.info("Create shaped JSON recipe")

        # pattern
        self.result["pattern"] = self.recipe.pattern

        # item ingredients
        for key, value in self.recipe.item_input.items():
            self.result["key"][key] = {}
            self.result["key"].get(key)["item"] = value

        # block ingredients
        for key, value in self.recipe.block_input.items():
            self.result["key"][key] = {}
            self.result["key"].get(key)["block"] = value

        # recipe output
        output = self.recipe.output
        self.result["result"]["item"] = output
        self.result["result"]["count"] = int(self.recipe.output_count)

    def create_shapeless_json(self) -> None:
        """Creates a shapeless recipe json using given recipe class.
        """
        self.logger.info("Create shapeless JSON recipe")

        # item ingredients
        for value in self.recipe.item_input:
            self.result["ingredients"].append({"item": value})

        # block ingredients
        for value in self.recipe.block_input:
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
        self.logger.info("Create JSON recipe file at given file location")

        path = join(base_path, self.recipe.name + '.json')
        with open(path, 'w') as outfile:
            dump(self.result, outfile)

        if exists(path):
            return True
        else:
            self.logger.error("File creation failed")
            return False
