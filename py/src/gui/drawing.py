from dataclasses import dataclass

import pygame

from engine.board import Entity, EvaluatedBoard, Unit
from engine.shared import Coord

# the engine renders the game at a reduced resolution of `dimension`, however the drawing module needs to blow up the resolution to a higher resolution,
# this is done using `scale`,

# def new_turtle() -> Turtle:
#     dw = Turtle()
#     dw.hideturtle()
#     return dw


# def draw_polygon(dw: Turtle, size: float, sides: int, angle: float):
#     for _ in range(0, sides):
#         dw.forward(size)
#         dw.right(angle)


# def draw_square(dw: Turtle, size: float):
#     draw_polygon(dw, size, 4, 90)


# def go(dw: Turtle, position: Coord):
#     dw.penup()
#     dw.setposition(position)
#     dw.pendown()


# @dataclass
class Drawer:
    def __init__(self, scale: float, dimensions: Coord):
        self.scale = scale
        self.dimensions = dimensions
        pygame.init()
        self.screen = pygame.display.set_mode(
            self.dimensions
            # (self.dimensions[0] * self.scale, self.dimensions[1] * self.scale)
        )
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
        print(f"drawing rectangle at {(rx, ry)}:{(lx, ly)}")
        pygame.draw.rect(
            self.screen, color, pygame.Rect(lx, ly, side_length, side_length)
        )

    def draw_apple(self, coord: Coord):
        # print(f"drew apple at {coord}")
        self.draw_pixel(coord, "red")
        # dw = new_turtle()
        # go(dw, coord)

        # dw.fillcolor("red")
        # dw.begin_fill()
        # dw.circle(self.scale)
        # dw.end_fill()

    def draw_snake_body(self, coord: Coord):
        # print(f"drew snake body at {coord}")
        self.draw_pixel(coord, "green")
        # dw = new_turtle()
        # go(dw, coord)

        # dw.fillcolor("green")
        # dw.begin_fill()
        # draw_square(dw, self.scale)
        # dw.end_fill()

    def draw_snake_head(self, coord: Coord):
        self.draw_snake_body(
            coord
        )  # for now snake head is rendered the same as snake body

    def draw_empty(self, coord: Coord):
        # self.draw_rectangle(coord, "yellow")
        pass
        # print(f"drew empty at {coord}")
        # if False:
        #     dw = new_turtle()
        #     go(dw, coord)
        #     dw.pencolor("red")
        #     dw.fillcolor("black")
        #     dw.begin_fill()
        #     draw_square(dw, self.scale)
        #     dw.end_fill()

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
            # t = new_turtle()
            # go(t, (0, i))
            # t.right(90)
            # t.forward(90)
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
        # rect.center = (self.dimensions[0] // 2, self.dimensions[1] // 2)
        rect.center = self.from_cartesian((0, 0))
        self.screen.blit(rendered_text, rect)
        pass
        # dw = new_turtle()
        # go(dw, (int(-self.scale * 10), int(self.scale * 10)))
        # dw.fillcolor("grey")
        # dw.pencolor("black")
        # draw_square(dw, self.scale * 10)
        # go(dw, (0, 0))
        # dw.write(text, align="center")

    def draw_start(self):
        self.draw_dialog("Play!")

    def draw_pause(self):
        self.draw_dialog("Unpause")

    def update(self):
        pygame.display.flip()

    def clear(self):
        self.screen.fill("black")

    # def show_results(self, state:State):
    #     pass
