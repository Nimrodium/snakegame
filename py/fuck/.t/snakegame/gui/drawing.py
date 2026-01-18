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
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.clear()

    def draw_rectangle(self, coord: Coord, color: str):
        print(f"drawing rectangle at {coord}")
        (x_lb, y_lb) = (coord[0] * self.scale, coord[1] * self.scale)
        (x_rt, y_rt) = ((coord[0] + 1) * self.scale, (coord[1] + 1) * self.scale)
        pygame.draw.rect(self.screen, color, pygame.Rect(x_lb, y_lb, x_rt, y_rt))

    def draw_apple(self, coord: Coord):
        print(f"drew apple at {coord}")
        # dw = new_turtle()
        # go(dw, coord)

        # dw.fillcolor("red")
        # dw.begin_fill()
        # dw.circle(self.scale)
        # dw.end_fill()

    def draw_snake_body(self, coord: Coord):
        print(f"drew snake body at {coord}")
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
                self.draw(unit)

    def draw_dialog(self, text: str):
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
