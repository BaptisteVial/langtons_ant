import logging

logger = logging.getLogger("LangtonsAnt")

class Grid:
    def __init__(self):
        """Initializes an empty infinite grid (all tiles are white by default)."""
        self._tiles = {}  # Dictionary to store black tiles (white tiles are implicitly defined)
        logger.debug("Grid initialized.")

    def flip_tile(self, x: int, y: int):
        """Flips the color of a tile (white <-> black)."""
        if (x, y) in self._tiles: # Condition of being a black tile
            logger.info(f"Flipping tile at ({x}, {y}) from black to white.")
            del self._tiles[(x, y)]  # Turn black tile to white
        else:
            logger.info(f"Flipping tile at ({x}, {y}) from white to black.")
            self._tiles[(x, y)] = True  # Turn white tile to black

    def is_white(self, x: int, y: int) -> bool:
        """Returns True if the tile at (x, y) is white, False if black."""
        is_white = (x, y) not in self._tiles
        logger.debug(f"Tile at ({x}, {y}) is {'white' if is_white else 'black'}.")
        return is_white

    def get_black_tiles(self) -> list[tuple[int, int]]:
        """Returns a list of all black tile coordinates."""
        black_tiles = list(self._tiles.keys())
        logger.debug(f"Current black tiles: {black_tiles}")
        return black_tiles
 