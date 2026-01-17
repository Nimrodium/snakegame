from dataclasses import dataclass
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


class Board:
    def __init__(self, dimensions: Coord):
        self.snake = Snake.new(dimensions)
        self.dimensions = dimensions
        self.apple = (0, 0)
        self.spawn_apple()

    def spawn_apple(self):
        (xbound, ybound) = self.dimensions
        rand = Random()
        adjecents: list[Coord] = []
        (xapple, yapple) = self.apple
        for y in range(-1, 2):
            for x in range(-1, 2):
                adjecents.append((xapple + x, yapple + y))

        while True:
            position = int(rand.random() * xbound), int(rand.random() * ybound)
            if (
                position != self.apple
                and position not in self.snake.segments
                and position not in adjecents
            ):
                self.apple = position
                break

    def evaluate_state(
        self, direction: Direction
    ) -> tuple[EvaluatedBoard, bool, bool]:  # ate_apple,collision
        ate_apple: bool = self.snake.get_head() == self.apple
        collision: bool = self.snake.collision()
        if ate_apple:
            self.spawn_apple()
        self.snake.advance(direction)
        return (self.render(), ate_apple, collision)

    def render(self) -> EvaluatedBoard:
        (xbound, ybound) = self.dimensions
        rows: EvaluatedBoard = []
        for row in range(0, ybound + 1):
            eval_row: list[Unit] = []
            for column in range(0, xbound):
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
