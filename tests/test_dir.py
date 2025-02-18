import pytest
from langtons_ant.dir import Dir

def test_dir_turns():
    assert Dir.UP.turn_right() == Dir.RIGHT
    assert Dir.RIGHT.turn_right() == Dir.DOWN
    assert Dir.DOWN.turn_right() == Dir.LEFT
    assert Dir.LEFT.turn_right() == Dir.UP

    assert Dir.UP.turn_left() == Dir.LEFT
    assert Dir.LEFT.turn_left() == Dir.DOWN
    assert Dir.DOWN.turn_left() == Dir.RIGHT
    assert Dir.RIGHT.turn_left() == Dir.UP