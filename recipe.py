class ShapelessRecipe:

    def __init__(self, name, output, ingredient):
        self._name = name
        self._output = output
        self._ingredient = ingredient

    def __str__(self):
        return "Name: %s\nOutput: %s\nIngredients: %s" % (
            self._name, self._output, self._ingredient)

    def get_name(self):
        return self._name

    def get_output(self):
        return self._output

    def get_ingredient(self):
        return self._ingredient

    def get_type(self):
        return "minecraft:crafting_shapeless"


class ShapedRecipe:

    def __init__(self, name, output, item_input, pattern, block_input=None):
        self._name = name
        self._output = output
        self._item_input = item_input
        self._block_input = block_input
        self._pattern = pattern
        self._type = "crafting_shaped"

    def __str__(self):
        return "Name: %s\nOutput: %s\nItem Input: %s\nBlock Input: %s\nPattern: %s\n" % (
            self._name, self._output, self._item_input, self._block_input, self._pattern)

    def get_name(self):
        return self._name

    def get_output(self):
        return self._output

    def get_item_input(self):
        return self._item_input

    def get_block_input(self):
        return self._block_input

    def get_pattern(self):
        return self._pattern

    def get_type(self):
        return "minecraft:" + self._type

