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
    pygame.init()
    SCREENWIDTH = 800
    SCREENHEIGHT = 800
    RED = (255, 0, 0)
    screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    pygame.draw.rect(screen, RED, (400, 400, 20, 20), 0)
    screen.fill(RED)

    pygame.display.update()

    # waint until user quits
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    # board = Board(dimensions)
    # print(f"apple pos: {board.apple}")
    # print(f"snake_head pos: {board.snake.get_head()}")
    # drawer = Drawer(scale, dimensions)
    # drawer.draw_rectangle((0, 0), "green")
    # drawer.update()
    # while True:
    #     pass  # keep alive
    # for i in range(0, 10):
    #     print(f"Frame {i + 1}")
    #     drawer.draw_board(board.evaluate_state(Direction.Left)[0])
    #     drawer.update()
    #     drawer.clear()
    # sleep(frame_rate * 0.001)

    # drawer.draw_snake_body((0, 0))


def main():
    scale = 10
    dimensions = (100, 100)
    frame_rate = 60
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    print("Available drivers:", pygame.display.list_modes())
    print("Current driver:", pygame.display.get_driver())
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    # test(scale, dimensions, frame_rate)
    # game = Game.initialize((100, 100), 1, 25, keybinds)
    # game.loop()


if __name__ == "__main__":
    main()
