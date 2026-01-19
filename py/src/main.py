from dataclasses import dataclass
from enum import Enum, auto
from time import sleep, time

import pygame

from engine.board import Board
from engine.shared import Coord, Direction
from game import Game
from gui.drawing import Drawer
from gui.input import Input, Key

keybindings = {
    pygame.K_w: Key.Up,
    pygame.K_s: Key.Down,
    pygame.K_a: Key.Left,
    pygame.K_d: Key.Right,
    pygame.K_q: Key.Exit,
    pygame.QUIT: Key.Exit,
    pygame.K_UP: Key.Up,
    pygame.K_DOWN: Key.Down,
    pygame.K_LEFT: Key.Left,
    pygame.K_RIGHT: Key.Right,
    pygame.K_SPACE: Key.PlayPause,
}


def test(scale: int, dimensions: Coord, frame_rate: int):
    board = Board(dimensions, scale)
    print(f"apple pos: {board.apple}")
    print(f"snake_head pos: {board.snake.get_head()}")
    drawer = Drawer(scale, dimensions)

    # for x in range(board.apple[0], 100):
    #     drawer.draw_rectangle((x, 0), "green")
    # for y in range(board.apple[1], 100):
    #     drawer.draw_rectangle((0, y), "red")
    # drawer.draw_rectangle((0, 0), "green")
    # drawer.draw_rectangle((10, 10), "green")
    # drawer.draw_rectangle((10, -10), "green")
    # corners = [(-200, -200), (200, 200), (-200, 200), (200, -200)]
    # colors = ["green", "red", "yellow", "blue"]
    # for corner, color in zip(corners, colors):
    #     # corner = (corner[0] - 20, corner[1] - 10)

    #     drawer.draw_rectangle(corner, color)
    #     drawer.update()
    eval_board = board.evaluate_state(Direction.Left)[0]
    # print(eval_board)
    drawer.draw_board(eval_board)
    drawer.update()
    # drawer.update()
    for i in range(0, 50):
        print(f"Frame {i + 1}")
        # board.spawn_apple()
        drawer.draw_board(board.evaluate_state(Direction.Down)[0])
        drawer.update()
        drawer.clock.tick(frame_rate)
        drawer.clear()

    # drawer.draw_snake_body((0, 0))


def main():
    scale = 15
    dimensions = (500, 500)
    frame_rate = 10
    # test(scale, dimensions, frame_rate)
    Game.initialize(dimensions, scale, frame_rate, keybindings).loop()


if __name__ == "__main__":
    main()
