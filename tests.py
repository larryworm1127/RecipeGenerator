from json_generator import Json
from recipe import ShapedRecipe, ShapelessRecipe

recipe_one = ShapedRecipe("block_copper", ("block", "equipmentaddtion:block_copper"),
                          {'C': "equipmentaddition:ingot_copper"},
                          None, ["CCC", "CCC", "CCC"])
recipe_two = ShapedRecipe("mithril_sword", ("block", "equipmentaddtion:mithril_sword"),
                          {'M': "equipmentaddition:ingot_mithril", 'S': "minecraft:stick"},
                          None, [" M ", " M ", " S "])

recipe_three = ShapelessRecipe("ingot_bronze", ("item", "equipmentaddtion:ingot_bronze"),
                               ["equipmentaddtition:ingot_tin", "equipmentaddition:ingot_copper"],
                               None)
recipe_four = ShapelessRecipe("ingot_mithril", ("item", "equipmentaddtion:ingot_mithril"),
                              ["equipmentaddtition:ingot_silver", "equipmentaddition:ingot_steel"],
                              None)


class TestShapedRecipe:
    def __init__(self):
        self._test_one = recipe_one
        self._test_two = recipe_two

    def test_str(self):
        print(self._test_one)
        print(self._test_two)


a = TestShapedRecipe()
# print(a.test_str())


class TestShapelessRecipe:
    def __init__(self):
        self._test_one = recipe_three
        self._test_two = recipe_four

    def test_str(self):
        print(self._test_one)
        print(self._test_two)


c = TestShapelessRecipe()
print(c.test_str())


class TestJson:
    def __init__(self):
        self._test_one = Json(recipe_one)
        self._test_two = Json(recipe_two)
        self._test_three = Json(recipe_three)
        self._test_four = Json(recipe_four)

    def test_str(self):
        print(self._test_one)
        print(self._test_two)
        print(self._test_three)
        print(self._test_four)


b = TestJson()
print(b.test_str())
