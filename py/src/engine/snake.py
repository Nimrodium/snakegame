# pure function which takes snake position and direction of travel and returns a snake advanced one frame
from dataclasses import dataclass, field

from engine.shared import Coord, Direction


# @dataclass
class Snake:
    # first segment is tail, last segment is head
    def __init__(self, dimensions: Coord):
        self.dimensions: Coord = dimensions
        self.will_grow: bool = False
        self.last_direction: Direction = Direction.Last
        self.segments: list[Coord] = self.initial_position()

    @staticmethod
    def initial_position() -> list[Coord]:
        return [(0, 0), (1, 0), (2, 0)]

    # def new(dimensions: Coord) -> "Snake":
    #     return Snake(dimensions)
    def reset(self):
        self.segments = self.initial_position()
        self.last_direction = Direction.Last
        self.will_grow = False

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
                    head = (hx + 0, hy + 0)
                else:
                    head = self.advance_head(self.last_direction)
        if direction != Direction.Last:
            self.last_direction = direction
            print(f"advancing head: {direction}")
        # print(f"last direction {self.last_direction}")
        return head

    def advance(self, direction: Direction):
        # if self.last_direction == Direction.Last and direction == Direction.Last:
        #     return
        if direction == Direction.Last:
            direction = self.last_direction
        else:
            self.last_direction = direction

        # if direction != Direction.Last:
        #     direction = self.last_direction
        # elif self.last_direction == Direction.Last:
        #     print("advance head No Op")
        #     return
        # else:
        #     self.last_direction = direction
        (hx, hy) = self.get_head()
        head: Coord
        print(f"2 advancing head: {direction}")
        match direction:
            case Direction.Up:
                head = (
                    (hx, hy + 1) if self.last_direction != Direction.Down else (hx, hy)
                )
            case Direction.Down:
                head = (hx, hy - 1) if self.last_direction != Direction.Up else (hx, hy)
            case Direction.Left:
                head = (
                    (hx - 1, hy) if self.last_direction != Direction.Right else (hx, hy)
                )
            case Direction.Right:
                head = (
                    (hx + 1, hy) if self.last_direction != Direction.Left else (hx, hy)
                )
            case Direction.Last:
                head = (hx, hy)
                # raise RuntimeError(f"unreachable case {direction}")
        if head != (hx, hy):
            self.delete_tail()
            self.add_head(head)

    def collision(self) -> bool:
        # will check if any snake segments share the same coordinate, or if it is out of bounds of the board.
        print(
            f"----- SEGMENTS:: {len(set(self.segments))} > {len(self.segments)}\n{self.segments}"
        )
        self_collision = len(set(self.segments)) < len(self.segments)
        bounds = tuple(map(lambda p: (-p, p), map(lambda p: p // 2, self.dimensions)))
        ((xmin, xmax), (ymin, ymax)) = bounds
        print(f"{bounds=}")
        wall_collision = any(
            map(
                lambda p: p[0] < xmin or p[0] > xmax or p[1] < ymin or p[1] > ymax,
                self.segments,
            )
        )
        print(f"{self_collision=}\n{wall_collision=}")
        return self_collision or wall_collision
        # return False
