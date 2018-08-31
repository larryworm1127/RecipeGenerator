"""
Python module that contains two classes for Shaped and Shapeless recipes

@date: 5/16/2018
@author: Larry Shi
"""

# general import
from logging import Logger
from dataclasses import dataclass, field
from typing import Union

from . import util


# recipe classes
@dataclass
class ShapelessRecipe:
    # recipe variables
    name: str
    output: str
    item_input: Union[dict, None]
    block_input: Union[dict, None]
    output_count: int = 1
    type: str = "crafting_shapeless"

    # logging
    debug: bool = False
    logger: Logger = field(init=False)

    def __post_init__(self):
        self.logger = util.get_logger("recipe.ShapelessRecipe", self.debug)
        self.logger.info("Shapeless recipe object created")


@dataclass
class ShapedRecipe:
    # recipe variables
    name: str
    output: str
    item_input: Union[dict, None]
    block_input: Union[dict, None]
    pattern: list
    output_count: int = 1
    type: str = "crafting_shaped"

    # logging
    debug: bool = False
    logger: Logger = field(init=False)

    def __post_init__(self):
        self.logger = util.get_logger("recipe.ShapedRecipe", self.debug)
        self.logger.info("Shaped recipe object created")
