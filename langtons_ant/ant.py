import importlib.resources

import math
import logging
import pygame

from .dir import Dir
from .tile import Tile
from .grid import Grid

logger = logging.getLogger("LangtonsAnt")

class Ant:
    "Handles the ant."

    def __init__(self, row: int , colon: int , direction : Dir) -> None:
        """Initializes the ant at (row, colon) facing DIR."""
        self._x = row
        self._y = colon
        self._direction = direction
        logger.debug(f"Ant initialized at ({row}, {colon}) facing {direction}.")

    def move(self):
        """Moves the ant one step forward in its current direction."""
        dx, dy = self._direction.value
        self._x += dx
        self._y += dy
        logger.debug(f"Ant moved to ({self._x}, {self._y})")

    def turn(self, turn_right: bool):
        old_direction = self._direction
        if turn_right:
            self._direction = self._direction.turn_right()
        else:
            self._direction = self._direction.turn_left()
        logger.info(f"Ant turned {'right' if turn_right else 'left'}: {old_direction} -> {self._direction}")

    @property
    def position(self) -> tuple[int, int]:
        """Returns the current position of the ant."""
        return self._x, self._y

    @property
    def direction(self) -> Dir:
        """Returns the current direction of the ant."""
        return self._direction