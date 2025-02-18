import pytest
from langtons_ant.grid import Grid

def test_grid_initialization():
    """Test if the grid initializes correctly as empty (all tiles white)."""
    grid = Grid()
    assert grid.get_black_tiles() == []

def test_grid_flip_tile():
    """Test flipping tiles from white to black and back."""
    grid = Grid()
    grid.flip_tile(2, 3)
    assert not grid.is_white(2, 3)  # Tile should be black
    grid.flip_tile(2, 3)
    assert grid.is_white(2, 3)  # Tile should be white again

def test_grid_black_tiles_list():
    """Test that black tiles are correctly stored."""
    grid = Grid()
    grid.flip_tile(0, 0)
    grid.flip_tile(1, 1)
    assert set(grid.get_black_tiles()) == {(0, 0), (1, 1)}

def test_grid_removes_black_tile():
    """Test that a black tile is removed when flipped back to white."""
    grid = Grid()
    grid.flip_tile(5, 5)  # Turn black
    grid.flip_tile(5, 5)  # Turn back to white
    assert grid.is_white(5, 5)
    assert (5, 5) not in grid.get_black_tiles()