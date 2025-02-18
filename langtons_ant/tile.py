# Third party
import pygame
import logging

# First party
from .dir import Dir

logger = logging.getLogger("LangtonsAnt")

class Tile:
    """
    A square tile in the game.

    Includes a color.
    """

    def __init__(self, x: int, y: int, color: pygame.Color) -> None:
        """Object initialization."""
        self._x = x # Column index
        self._y = y # Line index
        self._color = color
        logger.debug(f"Tile created at ({x}, {y}) with color {color}")

    @property
    def x(self) -> int:
        """The x coordinate (i.e.: column index) of the tile."""
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """Set the x coordinate."""
        self._x = value

    @property
    def y(self) -> int:
        """The y coordinate (i.e.: line index) of the tile."""
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        """Set the y coordinate."""
        self._y = value

    @property
    def color(self) -> pygame.Color:
        """The color of the tile."""
        return self._color

    @color.setter
    def color(self, color: pygame.Color) -> None:
        """Change the color of the tile."""
        self._color = color
        logger.info(f"Changing tile color at ({self._x}, {self._y}) from {self._color} to {color}")

    def __eq__(self, other: object) -> bool:
        """
        Check if two tiles are equal.

        Compare the x and y coordinates.
        """
        if isinstance(other, Tile):
            equal = self._x == other._x and self._y == other._y
            logger.debug(f"Tile equality check: {self} == {other} -> {equal}")
            return equal
        return False

    def __add__(self, other: object) -> "Tile":
        """Add two tiles together or a tile with a direction."""
        if isinstance(other, (Tile, Dir)):
            new_tile = Tile(x=self.x + other.x, y=self.y + other.y, color=self.color)
            logger.debug(f"Adding {self} + {other} -> {new_tile}")
            return new_tile
        msg = f"Wrong object type {type(other)}."
        logger.error(msg)
        raise ValueError(msg)

    def __sub__(self, other: object) -> "Tile":
        """Substract a tile or a direction to this tile."""
        if isinstance(other, (Tile, Dir)):
            new_tile = Tile(x=self.x - other.x, y=self.y - other.y, color=self.color)
            logger.debug(f"Subtracting {self} - {other} -> {new_tile}")
            return new_tile
        msg = f"Wrong object type {type(other)}."
        logger.error(msg)
        raise ValueError(msg)

    def draw(self, screen: pygame.Surface, size: int) -> None:
        """Draw the tile on screen."""
        rect = pygame.Rect(self._x * size, self._y * size, size, size)
        pygame.draw.rect(screen, self.color, rect)
