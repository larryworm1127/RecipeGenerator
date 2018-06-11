"""
Python module that generates a JSON file for recipe created by the user

@date: 5/14/2018
@author: Larry Shi
"""

# general imports
from json import dump
from os.path import join, expanduser, exists

# constants
RECIPE_PATH = expanduser('~')


# json class
class Json:
    """Class for recipe json object"""

    def __init__(self, recipe):
        # initialize variables
        self._recipe = recipe
        self._name = self._recipe.get_name()
        self._type = self._recipe.get_type()

        # actions for shaped recipe
        if self._type == "crafting_shaped":
            self._result = {"type": "minecraft:" + self._type, "pattern": [], "key": {}, "result": {}}
            self.create_shaped_json()

        # actions for shapeless recipe
        else:
            self._result = {"type": "minecraft:" + self._type, "ingredients": [], "result": {}}
            self.create_shapeless_json()

    def __str__(self):
        # variables
        result = "{ \n"

        # format strings
        count = 1
        for key, item in self._result.items():
            # one item case - item is string
            if type(item) == str:
                result += "  " + repr(key) + ': ' + repr(item) + '\n'

            # multiple item case - item is dict
            elif type(item) == dict:
                result += "  " + repr(key) + ': { \n'

                # loop through the first inner dict
                count_inner = 1
                for item_key, value in item.items():

                    # inner dict item is not dict
                    if type(value) != dict:

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    " + repr(item_key) + ': ' + repr(value) + '\n'
                        else:
                            result += "    " + repr(item_key) + ': ' + repr(value) + ', \n'

                    # inner dict item is dict
                    else:
                        result += "    " + repr(item_key) + ': { \n'
                        count_inner_two = 1
                        for item_key_two, value_two in value.items():

                            # determine whether to add comma at the end or not
                            if count_inner_two == len(value):
                                result += "      " + repr(item_key_two) + ': ' + repr(value_two) + '\n'
                            else:
                                result += "      " + repr(item_key_two) + ': ' + repr(value_two) + ', \n'

                            count_inner_two += 1

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    } \n"
                        else:
                            result += "    }, \n"

                    count_inner += 1
                    
                # determine whether to add comma at the end or not
                if count == len(self._result):
                    result += "  } \n"
                else:
                    result += "  }, \n"

            # multiple item case - item is list
            else:
                result += "  " + repr(key) + ': [ \n'

                count_inner = 1
                for value in item:

                    # add string quotes around is value is string
                    if type(value) == str:

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    " + repr(value) + '\n'
                        else:
                            result += "    " + repr(value) + ", \n"

                    # don't add quotes around is value isn't a string
                    else:

                        # determine whether to add comma at the end or not
                        if count_inner == len(item):
                            result += "    " + repr(value) + "\n"
                        else:
                            result += "    " + repr(value) + ", \n"

                    count_inner += 1

                # determine whether to add comma at the end or not
                if count == len(self._result):
                    result += "  ] \n"
                else:
                    result += "  ], \n"

            count += 1

        result += "}"

        return result

    def get_json(self):
        """Get method for json resultant"""
        return self._result

    def get_name(self):
        """Get method for name of the recipe"""
        return self._name

    def create_shaped_json(self):
        """Method that creates a shaped recipe json using given recipe class"""

        # pattern
        self._result["pattern"] = self._recipe.get_pattern()

        # item ingredients
        item_input = self._recipe.get_item_input()
        if item_input is not None:
            for key, value in item_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["item"] = value

        # block ingredients
        block_input = self._recipe.get_block_input()
        if block_input is not None:
            for key, value in block_input.items():
                self._result["key"][key] = {}
                self._result["key"][key]["block"] = value

        # recipe output
        output = self._recipe.get_output()
        self._result["result"]["item"] = output
        self._result["result"]["count"] = int(self._recipe.get_count())

    def create_shapeless_json(self):
        """Method that creates a shapeless recipe json using given recipe class"""

        # item ingredients
        item_input = self._recipe.get_item_input()
        if item_input is not None:
            for value in item_input:
                self._result["ingredients"].append({"item": value})

        # block ingredients
        block_input = self._recipe.get_block_input()
        if block_input is not None:
            for value in block_input:
                self._result["ingredients"].append({"block": value})

        # recipe output
        output = self._recipe.get_output()
        self._result["result"]["item"] = output
        self._result["result"]["count"] = int(self._recipe.get_count())

    def generator(self, base_path):
        """
        Method that creates the json file with given dir path
        and the created resultant json

        :param base_path: the path of the directory
        :return: boolean of whether the file creation was successful
        """

        path = join(base_path, self._name + '.json')
        with open(path, 'w') as outfile:
            dump(self.get_json(), outfile)

        return True if exists(path) else False
