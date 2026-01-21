from dataclasses import dataclass
from enum import Enum, auto
from time import sleep, time

import pygame
import sys

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

def main():
    # basic bitch arg parsing
    scale = 15
    dimensions = (500, 500)
    frame_rate = 10
    # test(scale, dimensions, frame_rate)
    game = Game.initialize(dimensions, scale, frame_rate, keybindings)
    print(sys.argv)
    game.loop()
    # if sys.argv == "test":
    #     game.test()
    # else:
    #     game.loop()

if __name__ == "__main__":
    main()
