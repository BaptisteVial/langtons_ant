from .ant import Ant
from .grid import Grid
from .dir import Dir

import logging

logger = logging.getLogger("LangtonsAnt")

class Simulation:
    def __init__(self, row : int, colon : int, direction : Dir, steps: int):
        """Initializes the simulation with a given number of steps."""
        self._ant = Ant(row = row, colon = colon, direction = direction)
        self._grid = Grid()
        self._steps = steps
        logger.debug(f"Simulation initialized with {steps} steps.")

    def run(self):
        """Runs the Langton's Ant simulation for the specified steps."""
        logger.info("Starting simulation.")
        for step in range(self._steps):
            x, y = self._ant.position
            turn_right = self._grid.is_white(x, y) # returns True if the ant is on a white tile, False if not
            self._ant.turn(turn_right) # so the ant turns on the right if and only if the tile is white, turns left if not
            self._grid.flip_tile(x, y) # before leaving a the tile, the ant changes its color
            self._ant.move() # and then leaves
            logger.debug(f"Step {step + 1}/{self._steps}: Ant at {self._ant.position} facing {self._ant.direction}")

        logger.info("Simulation completed.")

    def get_state(self) -> str:
        """Returns the final state of the grid and ant as a string."""
        x, y = self._ant.position
        direction = self._ant.direction.name
        black_tiles = self._grid.get_black_tiles()
        min_x = min((t[0] for t in black_tiles), default=0)
        max_x = max((t[0] for t in black_tiles), default=0)
        min_y = min((t[1] for t in black_tiles), default=0)
        max_y = max((t[1] for t in black_tiles), default=0)
        grid_str = f"Step {self._steps}\n{x},{y},{direction}\n"
        for j in range(min_y, max_y + 1):
            row = "".join("X" if (i, j) in black_tiles else " " for i in range(min_x, max_x + 1))
            grid_str += row + "\n"
        return grid_str