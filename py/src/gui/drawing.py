from dataclasses import dataclass

import pygame

from engine.board import Entity, EvaluatedBoard, Unit
from engine.shared import Coord

# the engine renders the game at a reduced resolution of `dimension`, however the drawing module needs to blow up the resolution to a higher resolution,
# this is done using `scale`,


class Drawer:
    def __init__(self, scale: float, dimensions: Coord):
        self.scale = scale
        self.dimensions = dimensions
        pygame.init()
        self.screen = pygame.display.set_mode(self.dimensions)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("freesansbold.ttf", 16)
        self.clear()

    def from_cartesian(self, coord: Coord) -> Coord:
        (x, y) = coord
        (x, y) = (int(x * self.scale // 2), int(y * self.scale // 2))
        (dx, dy) = self.dimensions
        return (x + (dx // 2), (dy // 2) - y)

    def draw_pixel(self, coord: Coord, color: str):
        # coord is center of rectangle.
        side_length = self.scale // 2
        (x, y) = self.from_cartesian(coord)
        (lx, ly) = (x - side_length, y - side_length)  # bottom left corner
        (rx, ry) = (x + side_length, y + side_length)  # top right corner
        # print(f"drawing rectangle at {(rx, ry)}:{(lx, ly)}")
        pygame.draw.rect(
            self.screen, color, pygame.Rect(lx, ly, side_length, side_length)
        )

    def draw_apple(self, coord: Coord):
        self.draw_pixel(coord, "red")

    def draw_snake_body(self, coord: Coord):
        self.draw_pixel(coord, "green")

    def draw_snake_head(self, coord: Coord):
        self.draw_snake_body(
            coord
        )  # for now snake head is rendered the same as snake body

    def draw_empty(self, coord: Coord):
        pass

    def draw(self, unit: Unit):
        (coord, entity) = unit
        match entity:
            case Entity.Empty:
                self.draw_empty(coord)
            case Entity.Apple:
                # print(f"APPLE: {coord}")
                self.draw_apple(coord)
            case Entity.SnakeBody:
                self.draw_snake_body(coord)
            case Entity.SnakeHead:
                self.draw_snake_head(coord)

    def draw_board(self, board: EvaluatedBoard):
        for i, row in enumerate(board):
            for unit in row:
                if unit[1] != Entity.Empty:
                    print(unit)
                self.draw(unit)

    def draw_dialog(self, text: str):
        rendered_text = self.font.render(
            text,
            True,
            (255, 255, 255),
        )
        rect = rendered_text.get_rect()
        rect.center = self.from_cartesian((0, 0))
        self.screen.blit(rendered_text, rect)
        pass

    def draw_start(self):
        self.draw_dialog("Play!")

    def draw_dead(self, score: int):
        self.draw_dialog(f"You Died! Score: {score}")

    def draw_pause(self):
        self.draw_dialog("Unpause")

    def update(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill("black")

    # def show_results(self, state:State):
    #     pass
