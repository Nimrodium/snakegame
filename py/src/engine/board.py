from enum import Enum, auto
from random import Random

from engine.shared import Coord, Direction
from engine.snake import Snake


class Entity(Enum):
    SnakeHead = auto()
    SnakeBody = auto()
    Apple = auto()
    Empty = auto()


Unit = tuple[Coord, Entity]
EvaluatedBoard = list[list[Unit]]

i: int = -50


class Board:
    def __init__(self, dimensions: Coord, scale: float):
        MAGIC_RANDOM_SCALE_FACTOR = 2  # ??? no idea why i have to 2x it
        self.dimensions = (
            dimensions[0] // int(scale) * MAGIC_RANDOM_SCALE_FACTOR,
            dimensions[1] // int(scale) * MAGIC_RANDOM_SCALE_FACTOR,
        )
        self.snake = Snake(self.dimensions)
        # self.dimensions = dimensions
        self.apple = (0, 0)
        self.spawn_apple()

    def reset(self):
        self.snake.reset()
        self.spawn_apple()

    def spawn_apple(self):
        # global i
        # i += 1
        # self.apple = (i, i)
        # return
        (xbound, ybound) = self.dimensions
        rand = Random()
        # adjecents: list[Coord] = []
        (xapple, yapple) = self.apple
        # for y in range(-1, 2):
        #     for x in range(-1, 2):
        #         adjecents.append((xapple + x, yapple + y))

        adjacents = [
            (xapple + dx, yapple + dy) for dx in range(-1, -2) for dy in range(-1, 2)
        ]
        while True:
            position = (
                int((rand.random() * xbound) - (xbound // 2)),
                int((rand.random() * ybound) - (ybound // 2)),
            )
            # position = (250, 250)
            if (
                position != self.apple
                and position not in self.snake.segments
                and position not in adjacents
            ):
                self.apple = position
                break

    def evaluate_state(
        self, direction: Direction
    ) -> tuple[EvaluatedBoard, bool, bool]:  # ate_apple,collision
        ate_apple: bool = self.snake.get_head() == self.apple
        if ate_apple:
            self.snake.grow()
            self.spawn_apple()
        self.snake.advance(direction)
        collision: bool = self.snake.collision()
        return (self.render(), ate_apple, collision)

    def render(self) -> EvaluatedBoard:
        (xbound, ybound) = self.dimensions
        rows: EvaluatedBoard = []
        for row in range(-ybound // 2, ybound // 2 + 1):
            eval_row: list[Unit] = []
            for column in range(-xbound // 2, xbound // 2 + 1):
                coord = (column, row)
                entity: Entity
                if coord == self.snake.get_head():
                    entity = Entity.SnakeHead
                elif coord == self.apple:
                    entity = Entity.Apple
                elif coord in self.snake.segments:
                    entity = Entity.SnakeBody
                else:
                    entity = Entity.Empty
                unit = (coord, entity)
                eval_row.append(unit)
            rows.append(eval_row)
        return rows
