from dataclasses import dataclass
from enum import Enum, auto
from time import time

import pygame
from pygame.event import Event

from engine.board import Board
from engine.shared import Coord
from gui.drawing import Drawer
from gui.input import Input, Key


class Scene(Enum):
    Start = auto()
    Dead = auto()
    Paused = auto()
    Playing = auto()
    Exiting = auto()


@dataclass
class State:
    apples_ate: int
    start_time: int
    scene: Scene
    time = 0

    # start_time:int = int(time.time())
    def update_time(self):
        diff = int(time()) - self.start_time
        self.time += diff

    def add_apple(self):
        self.apples_ate += 1


@dataclass
class Game:
    board: Board
    drawer: Drawer
    key_input: Input
    frame_rate: int
    last_input = Key.Null

    @staticmethod
    def initialize(
        dimensions: Coord, scale: float, frame_rate: int, keybindings: dict[int, Key]
    ) -> "Game":
        return Game(
            Board(dimensions, scale),
            Drawer(scale, dimensions),
            Input(keybindings),
            frame_rate,
        )

    def get_input(self) -> Key:
        user_input = self.key_input.get_input()
        if user_input == Key.Null:
            return self.last_input
        else:
            return user_input
    # benchmark one frame of a 15 length snake
    def benchmark(self) -> int:
        def avg(xs:list[int]) -> float:
            sum(xs)/len(xs)
        direction = Direction.Up
        logic_times : list[int] = []
        frame_times : list[int] = []
        for i in range(0,15):
            (x,y) = self.snake.get_head()
            self.snake.add_head((x+1,y))
        for _ in range(0,100):
            l_start = time()
            evaluated,_,_ = self.engine.evaluate_state(direction)
            f_start = time()
            self.drawer(evaluated)
            end = time()
            logic_times.append(end - l_start)
            frame_times.append(end - f_start)
        avg_logic = avg(logic_times)
        avg_frame = avg(frame_times)
        avg_total = avg_logic+avg_frame
        print(f"completed 100 frames of 15 length snake in {avg_total}; {avg_frame=}; {avg_logic=}")
    def step(self, state: State) -> State:
        user_input = self.get_input()
        match user_input:
            case Key.Exit:
                state.scene = Scene.Exiting
        print(user_input)
        match state.scene:
            case Scene.Exiting:
                pass
                # raise RuntimeError("IllegalState: cannot step when exiting")
            case Scene.Paused:
                if user_input == Key.PlayPause:
                    state.scene = Scene.Playing
                else:
                    self.drawer.draw_pause()
            case Scene.Start:
                if user_input == Key.PlayPause:
                    state.scene = Scene.Playing
                else:
                    self.drawer.draw_start()
            case Scene.Playing:
                if user_input == Key.PlayPause:
                    state.scene = Scene.Paused
                else:
                    evaluated, ate_apple, collision = self.board.evaluate_state(
                        user_input.to_direction()
                    )
                    if ate_apple:
                        state.add_apple()
                    self.drawer.draw_board(evaluated)
                    if collision:
                        print("You Died!")
                        state.scene = Scene.Dead
            case Scene.Dead:
                if user_input == Key.PlayPause:
                    self.board.reset()
                    state.scene = Scene.Playing
                else:
                    self.drawer.draw_dead(state.apples_ate)

        return state

    def loop(self) -> State:
        state = State(0, 0, Scene.Start)
        # start = time()
        while True:
            try:
                self.drawer.clear()
                print(f"State Scene: {state.scene} -- Time: {state.time}")
                state = self.step(state)
                if state.scene == Scene.Exiting:
                    break
                state.update_time()
                self.drawer.update()
                self.drawer.clock.tick(self.frame_rate)
                # sleep(self.frame_rate / 100)
            except KeyboardInterrupt:
                print("\nexiting...")
                break
        return state
