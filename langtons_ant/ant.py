from .dir import Dir

class Ant:
    def __init__(self, x: int = 0, y: int = 0):
        """Initializes the ant at (x, y) facing UP."""
        self._x = x
        self._y = y
        self._direction = Dir.UP

    def move(self):
        """Moves the ant one step forward in its current direction."""
        dx, dy = self._direction.value
        self._x += dx
        self._y += dy

    def turn(self, turn_right: bool):
        """Turns the ant based on the tile color (right for white, left for black)."""
        self._direction = self._direction.turn_right() if turn_right else self._direction.turn_left()

    @property
    def position(self) -> tuple[int, int]:
        """Returns the current position of the ant."""
        return self._x, self._y

    @property
    def direction(self) -> Dir:
        """Returns the current direction of the ant."""
        return self._direction