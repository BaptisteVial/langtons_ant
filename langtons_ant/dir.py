# Standard
import enum

class Dir(enum.Enum):
    """Direction of movement."""

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0) 

    @property
    def x(self) -> int:
        """Column index (starts at 0)."""
        return self.value[0]

    @property
    def y(self) -> int:
        """Line index (starts at 0)."""
        return self.value[1]
    
    def turn_right(self) -> "Dir":
        """Returns the new direction when turning right."""
        directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
        return directions[(directions.index(self) + 1) % 4]

    def turn_left(self) -> "Dir":
        """Returns the new direction when turning left."""
        directions = [Dir.UP, Dir.RIGHT, Dir.DOWN, Dir.LEFT]
        return directions[(directions.index(self) - 1) % 4]
