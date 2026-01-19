from enum import Enum, auto

# GAME_WIDTH: int = 100
# GAME_HEIGHT: int = 100
Coord = tuple[int, int]


class Direction(Enum):
    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()
    Last = auto()
