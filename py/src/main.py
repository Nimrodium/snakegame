from dataclasses import dataclass
from enum import Enum, auto
from time import sleep, time

from engine.board import Board
from engine.shared import Coord, Direction
from gui.drawing import Drawer
from gui.input import Input, Key

keybinds = {
    "w": Key.Up,
    "s": Key.Down,
    "a": Key.Left,
    "d": Key.Right,
    "q": Key.Exit,
    "Up": Key.Up,
    "Down": Key.Down,
    "Left": Key.Left,
    "Right": Key.Right,
    "space": Key.PlayPause,
}


import pygame
from pygame.locals import *


def test(scale: int, dimensions: Coord, frame_rate: int):
    board = Board(dimensions)
    print(f"apple pos: {board.apple}")
    print(f"snake_head pos: {board.snake.get_head()}")
    drawer = Drawer(scale, dimensions)
    # drawer.draw_rectangle((0, 0), "green")
    drawer.draw_rectangle((20, 20), "green")
    # drawer.draw_board(board.evaluate_state(Direction.Left)[0])
    # drawer.update()
    # for i in range(0, 10):
    #     print(f"Frame {i + 1}")
    #     drawer.draw_board(board.evaluate_state(Direction.Left)[0])
    #     drawer.update()
    #     drawer.clock.tick(60)
    #     drawer.clear()

    # drawer.draw_snake_body((0, 0))
    while True:
        pass


def main():
    scale = 20
    dimensions = (100, 100)
    frame_rate = 60
    test(scale, dimensions, frame_rate)


if __name__ == "__main__":
    main()
