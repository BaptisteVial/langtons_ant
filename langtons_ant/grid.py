class Grid:
    def __init__(self):
        """Initializes an empty infinite grid (all tiles are white by default)."""
        self._tiles = {}  # Dictionary to store black tiles (white tiles are implicitly defined)

    def flip_tile(self, x: int, y: int):
        """Flips the color of a tile (white <-> black)."""
        if (x, y) in self._tiles: # Condition of being a black tile
            del self._tiles[(x, y)]  # Turn black tile to white
        else:
            self._tiles[(x, y)] = True  # Turn white tile to black

    def is_white(self, x: int, y: int) -> bool:
        """Returns True if the tile at (x, y) is white, False if black."""
        return (x, y) not in self._tiles

    def get_black_tiles(self) -> list[tuple[int, int]]:
        """Returns a list of all black tile coordinates."""
        return list(self._tiles.keys())