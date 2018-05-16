from recipe import ShapedRecipe
from json_generator import Json

recipe_one = ShapedRecipe("block_copper", ("block", "equipmentaddtion:block_copper"),
                          {'C': "equipmentaddition:ingot_copper"},
                          ["CCC", "CCC", "CCC"])
recipe_two = ShapedRecipe("mithril_sword", ("block", "equipmentaddtion:mithril_sword"),
                          {'M': "equipmentaddition:ingot_mithril", 'S': "minecraft:stick"},
                          [" M ", " M ", " S "])


class TestShapedRecipe:
    def __init__(self):
        self._test_one = recipe_one
        self._test_two = recipe_two

    def test_str(self):
        print(self._test_one)
        print(self._test_two)


a = TestShapedRecipe()


# print(a.test_str())


class TestJson:
    def __init__(self):
        self._test_one = Json(recipe_one)
        self._test_two = Json(recipe_two)

    def test_str(self):
        print(self._test_one)
        print(self._test_two)


b = TestJson()
print(b.test_str())
