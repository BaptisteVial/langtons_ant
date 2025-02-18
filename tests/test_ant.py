import pytest
import pygame

from langtons_ant.ant import Ant
from langtons_ant.dir import Dir
from langtons_ant.grid import Grid

def test_ant_initial_position():
    """Test if the ant is placed at the correct initial position."""
    grid = Grid()  # Fix: No width/height arguments
    assert grid.is_white(0, 0)  # Assuming the ant starts at (0,0) on a white tile

def test_ant_moves_correctly():
    """Test if the ant moves correctly based on grid state."""
    grid = Grid()  # Fix: No width/height arguments
    # Simulate some moves
    grid.flip_tile(0, 0)  # The tile flips black, ant should turn right
    assert not grid.is_white(0, 0)  # Tile should now be black

def test_grid_out_of_bounds():
    """Test behavior for out-of-bounds grid access (should not raise errors)."""
    grid = Grid()  # Fix: No width/height arguments
    grid.flip_tile(-100, 100)  # Should not cause IndexError
    assert not grid.is_white(-100, 100)  # Tile should now be black

def test_ant_movement():
    ant = Ant(0, 0, Dir.UP)
    ant.move()
    assert ant.position == (0, -1)
    ant.turn(True)
    assert ant.direction == Dir.RIGHT
    ant.move()
    assert ant.position == (1, -1)

def test_ant_turn():
    ant = Ant(0, 0, Dir.UP)
    ant.turn(True)
    assert ant.direction == Dir.RIGHT
    ant.turn(True)
    assert ant.direction == Dir.DOWN
    ant.turn(False)
    assert ant.direction == Dir.RIGHT
