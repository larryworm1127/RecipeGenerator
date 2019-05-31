"""
Python module that contains two classes for Shaped and Shapeless recipes

@date: 5/16/2018
@author: Larry Shi
"""

# general import
from copy import copy
from logging import Logger
from typing import Union, List, Dict

from . import get_logger

__all__ = ["ShapelessRecipe", "ShapedRecipe"]


# recipe classes
class ShapelessRecipe:
    """A class representing a shapeless Minecraft recipe.
    """
    name: str
    output: str
    output_count: int
    debug: bool
    logger: Logger
    item_input: Union[List[str], Dict[str, str]]
    block_input: Union[List[str], Dict[str, str]]
    type: str

    def __init__(self,
                 name: str,
                 output: str,
                 item_input: Union[List[str], Dict[str, str]],
                 block_input: Union[List[str], Dict[str, str]],
                 output_count: int = 1,
                 debug: bool = False) -> None:
        """Shapeless recipe initializer.
        """
        # Recipe attributes
        self.name = name
        self.output = output
        self.output_count = output_count
        self.item_input = copy(item_input)
        self.block_input = copy(block_input)
        self.debug = debug
        self.type = "crafting_shapeless"

        # Logger
        self.logger = get_logger("recipe.recipe", self.debug)
        self.logger.info("Shapeless recipe object created")


class ShapedRecipe(ShapelessRecipe):
    """A class representing a shaped Minecraft recipe.
    """
    item_input: Dict[str, str]
    block_input: Dict[str, str]
    pattern: list

    def __init__(self,
                 name: str,
                 output: str,
                 item_input: Dict[str, str],
                 block_input: Dict[str, str],
                 pattern: List[str],
                 count: int = 1,
                 debug: bool = False) -> None:
        """Shaped recipe initializer.
        """
        super().__init__(name, output, item_input, block_input, count, debug)
        self.pattern = copy(pattern)
        self.type = "crafting_shaped"
        self.logger.info("Shaped recipe object created")
