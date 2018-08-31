"""
Python module that generates a JSON file for recipe created by the user

@date: 5/14/2018
@author: Larry Shi
"""

# general imports
from json import dump
from os.path import join, expanduser, exists
from typing import NoReturn, Union

from . import util, ShapelessRecipe, ShapedRecipe

# constants
RECIPE_PATH = expanduser('~')


# json class
class Json:
    """Class for recipe json object"""

    def __init__(self, recipe: Union[ShapedRecipe, ShapelessRecipe]):
        # initialize variables
        self._recipe = recipe
        self._name = recipe.name
        self._type = recipe.type
        self._logger = util.get_logger("recipe_json.Json", recipe.debug)

        # actions for shaped recipe
        if self._type == "crafting_shaped":
            self._result = {"type": "minecraft:" + self._type, "pattern": [], "key": {}, "result": {}}
            self.create_shaped_json()

        # actions for shapeless recipe
        else:
            self._result = {"type": "minecraft:" + self._type, "ingredients": [], "result": {}}
            self.create_shapeless_json()

    def __str__(self) -> str:
        self._logger.info("Create string representation of JSON recipe")

        # variables
        result = "{ \n"

        # format strings
        count = 1
        for key, item in self._result.items():
            # one item case - item is string
            if isinstance(item, str):
                result += "  {}: {} \n".format(repr(key), repr(item))

            # multiple item case - item is dict
            elif isinstance(item, dict):
                result += "  " + repr(key) + ': { \n'

                # loop through the first inner dict
                count_inner = 1
                for item_key, value in item.items():

                    # inner dict item is not dict
                    if isinstance(value, dict):
                        result += "    " + repr(item_key) + ': { \n'
                        count_inner_two = 1
                        for item_key_two, value_two in value.items():

                            # determine whether to add comma at the end or not
                            if count_inner_two == len(value):
                                result += "      {}: {} \n".format(repr(item_key_two), repr(value_two))
                            else:
                                result += "      {}: {}, \n".format(repr(item_key_two), repr(value_two))

                            count_inner_two += 1

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    } \n"
                        else:
                            result += "    }, \n"

                    # inner dict item is dict
                    else:

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    {}: {} \n".format(repr(item_key), repr(value))
                        else:
                            result += "    {}: {}, \n".format(repr(item_key), repr(value))

                    count_inner += 1

                # determine whether to add comma at the end or not
                if count == len(self._result):
                    result += "  } \n"
                else:
                    result += "  }, \n"

            # multiple item case - item is list
            else:
                result += "  {}: [ \n".format(repr(key))

                count_inner = 1
                for value in item:

                    # determine whether to add comma at the end or not
                    if count_inner == len(item):
                        result += "    {} \n".format(repr(value))
                    else:
                        result += "    {}, \n".format(repr(value))

                    count_inner += 1

                # determine whether to add comma at the end or not
                if count == len(self._result):
                    result += "  ] \n"
                else:
                    result += "  ], \n"

            count += 1

        result += "}"

        return result

    def get_json(self) -> dict:
        """Get method for json resultant"""

        return self._result

    def get_name(self) -> str:
        """Get method for name of the recipe"""

        return self._name

    def create_shaped_json(self) -> NoReturn:
        """Method that creates a shaped recipe json using given recipe class"""

        self._logger.info("Create shaped JSON recipe")

        # pattern
        self._result["pattern"] = self._recipe.pattern

        # item ingredients
        item_input = self._recipe.item_input
        if item_input is not None:
            for key, value in item_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["item"] = value

        # block ingredients
        block_input = self._recipe.block_input
        if block_input is not None:
            for key, value in block_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["block"] = value

        # recipe output
        output = self._recipe.output
        self._result["result"]["item"] = output
        self._result["result"]["count"] = int(self._recipe.output_count)

    def create_shapeless_json(self) -> NoReturn:
        """Method that creates a shapeless recipe json using given recipe class"""

        self._logger.info("Create shapeless JSON recipe")

        # item ingredients
        item_input = self._recipe.item_input
        if item_input is not None:
            for value in item_input:
                self._result["ingredients"].append({"item": value})

        # block ingredients
        block_input = self._recipe.block_input
        if block_input is not None:
            for value in block_input:
                self._result["ingredients"].append({"block": value})

        # recipe output
        output = self._recipe.output
        self._result["result"]["item"] = output
        self._result["result"]["count"] = int(self._recipe.output_count)

    def generator(self, base_path: str) -> bool:
        """
        Method that creates the json file with given dir path
        and the created resultant json

        :param base_path: the path of the directory
        :return: boolean of whether the file creation was successful
        """

        self._logger.info("Create JSON recipe file at given file location")

        path = join(base_path, self._name + '.json')
        with open(path, 'w') as outfile:
            dump(self.get_json(), outfile)

        if exists(path):
            return True
        else:
            self._logger.error("File creation failed")
            return False
