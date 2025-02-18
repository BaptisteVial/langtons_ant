import pygame
import pytest
from langtons_ant.tile import Tile

def test_tile_initialization():
    color = pygame.Color(255, 255, 255)
    tile = Tile(5, 10, color)
    
    assert tile.x == 5
    assert tile.y == 10
    assert tile.color == color

def test_tile_setters():
    color1 = pygame.Color(255, 255, 255)
    color2 = pygame.Color(0, 0, 0)
    tile = Tile(3, 6, color1)
    
    tile.x = 7
    tile.y = 8
    tile.color = color2
    
    assert tile.x == 7
    assert tile.y == 8
    assert tile.color == color2

def test_tile_addition():
    tile1 = Tile(2, 3, pygame.Color(255, 255, 255))
    tile2 = Tile(1, 1, pygame.Color(255, 255, 255))
    
    result = tile1 + tile2
    assert result.x == 3
    assert result.y == 4

def test_tile_color_change():
    """Test changing the tile color."""
    tile = Tile(4, 4, pygame.Color(255, 255, 255))  # White
    tile.color = pygame.Color(0, 0, 0)  # Change to black
    assert tile.color == pygame.Color(0, 0, 0)

def test_tile_equality():
    """Test that tiles with the same coordinates are considered equal."""
    tile1 = Tile(1, 2, pygame.Color(255, 255, 255))
    tile2 = Tile(1, 2, pygame.Color(0, 0, 0))
    assert tile1 == tile2  # Position matters, not color

def test_tile_math_operations():
    """Test adding and subtracting tiles."""
    tile1 = Tile(3, 3, pygame.Color(255, 255, 255))
    tile2 = Tile(1, 1, pygame.Color(255, 255, 255))

    sum_tile = tile1 + tile2
    assert sum_tile.x == 4
    assert sum_tile.y == 4

    sub_tile = tile1 - tile2
    assert sub_tile.x == 2
    assert sub_tile.y == 2
