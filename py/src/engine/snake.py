# pure function which takes snake position and direction of travel and returns a snake advanced one frame
from dataclasses import dataclass

from engine.shared import Coord, Direction


@dataclass
class Snake:
    # first segment is tail, last segment is head
    segments: list[Coord]
    will_grow: bool
    dimensions: Coord
    last_direction: Direction

    @staticmethod
    def new(dimensions: Coord) -> "Snake":
        return Snake([(0, 0), (1, 0), (2, 0)], False, dimensions, Direction.Last)

    def get_head(self) -> Coord:
        return self.segments[-1]  # thankfully nullsnake is not possible

    def get_tail(self) -> Coord:
        return self.segments[0]

    def delete_tail(self):
        if not self.will_grow:
            self.segments.pop(0)
        else:
            self.will_grow = False

    def add_head(self, head: Coord):
        self.segments.append(head)

    def grow(self):
        self.will_grow = True

    def advance_head(self, direction: Direction) -> Coord:
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
            case Direction.Last:
                if self.last_direction == Direction.Last:
                    head = (hx, hy)
                else:
                    head = self.advance_head(self.last_direction)

        if direction != Direction.Last:
            self.last_direction = direction
        print(f"last direction {self.last_direction}")
        return head

    def advance(self, direction: Direction):
        head = self.advance_head(direction)
        self.delete_tail()
        self.add_head(head)

    def collision(self) -> bool:
        # will check if any snake segments share the same coordinate, or if it is out of bounds of the board.
        return False
