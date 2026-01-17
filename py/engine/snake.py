# pure function which takes snake position and direction of travel and returns a snake advanced one frame
from dataclasses import dataclass

from engine.shared import Coord, Direction


@dataclass
class Snake:
    # first segment is tail, last segment is head
    segments: list[Coord]
    dimensions: Coord

    @staticmethod
    def new(dimensions: Coord) -> "Snake":
        return Snake([(0, 0), (1, 0), (2, 0)], dimensions)

    def get_head(self) -> Coord:
        return self.segments[-1]  # thankfully nullsnake is not possible

    def get_tail(self) -> Coord:
        return self.segments[0]

    def delete_tail(self):
        self.segments.pop(0)

    def add_head(self, head: Coord):
        self.segments.append(head)

    def advance(self, direction: Direction):
        (hx, hy) = self.get_head()
        head: Coord
        match direction:
            case Direction.Up:
                head = (hx, hy + 1)
            case Direction.Down:
                head = (hx, hy - 1)
            case Direction.Left:
                head = (hx - 1, hy)
            case Direction.Right:
                head = (hx + 1, hy)
        self.delete_tail()
        self.add_head(head)

    def collision(self) -> bool:
        return False
