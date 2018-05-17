# general imports
from unittest import TestCase
from os.path import exists, join

from recipe import ShapedRecipe, ShapelessRecipe
from json_generator import generator, Json, RECIPE_PATH

# objects
recipe_one = ShapedRecipe("block_copper", ("block", "equipmentaddtion:block_copper"),
                          {'C': "equipmentaddition:ingot_copper"},
                          None, ["CCC", "CCC", "CCC"])
recipe_two = ShapedRecipe("mithril_sword", ("block", "equipmentaddtion:mithril_sword"),
                          {'M': "equipmentaddition:ingot_mithril", 'S': "minecraft:stick"},
                          None, [" M ", " M ", " S "])
recipe_three = ShapelessRecipe("ingot_bronze", ("item", "equipmentaddtion:ingot_bronze"),
                               ["equipmentaddtition:ingot_tin", "equipmentaddition:ingot_copper"], None)
recipe_four = ShapelessRecipe("ingot_mithril", ("item", "equipmentaddtion:ingot_mithril"),
                              ["equipmentaddtition:ingot_silver", "equipmentaddition:ingot_steel"], None)


class TestShapedRecipe(TestCase):
    def test_str(self):
        self.assertTrue(recipe_one)
        self.assertTrue(recipe_two)


class TestShapelessRecipe(TestCase):
    def test_str(self):
        self.assertTrue(recipe_three)
        self.assertTrue(recipe_four)


class TestJson(TestCase):
    def test_str(self):
        self.assertTrue(Json(recipe_one))
        self.assertTrue(Json(recipe_two))
        self.assertTrue(Json(recipe_three))
        self.assertTrue(Json(recipe_four))

    def test_generator(self):
        json_one = Json(recipe_one)
        generator(json_one)
        self.assertTrue(exists(join(RECIPE_PATH, json_one.get_name() + '.json')))

        json_two = Json(recipe_two)
        generator(json_two)
        self.assertTrue(exists(join(RECIPE_PATH, json_two.get_name() + '.json')))

        json_three = Json(recipe_three)
        generator(json_three)
        self.assertTrue(exists(join(RECIPE_PATH, json_three.get_name() + '.json')))

        json_four = Json(recipe_four)
        generator(json_four)
        self.assertTrue(exists(join(RECIPE_PATH, json_four.get_name() + '.json')))
