import turtle
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


class Scene(Enum):
    Start = auto()
    PlayAgain = auto()
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
        dimensions: Coord, scale: float, frame_rate: int, keybindings: dict[str, Key]
    ) -> "Game":
        screen = turtle.Screen()
        screen.setup(width=scale * 10, height=scale * 10)
        return Game(Board(dimensions), Drawer(scale), Input(keybindings), frame_rate)

    def get_input(self) -> Key:
        user_input = self.key_input.get_input()
        if user_input == Key.Null:
            return self.last_input
        else:
            return user_input

    def step(self, state: State) -> State:
        user_input = self.get_input()
        match state.scene:
            case Scene.Exiting:
                raise RuntimeError("IllegalState: cannot step when exiting")
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
            case Scene.PlayAgain:
                if user_input == Key.PlayPause:
                    state.scene = Scene.Playing
                else:
                    self.drawer.draw_start()

        return state

        # if user_input == Key.Exit:
        #     return
        # if not start and not reset:
        #     evaluated, ate_apple = self.board.evaluate_state(user_input.to_direction())
        #     self.drawer.draw_board(evaluated)
        #     return
        # elif start:

    def loop(self) -> State:  # apples ate, time
        state = State(0, 0, Scene.Start)
        # start = time()
        while True:
            try:
                print(f"State Scene: {state.scene} -- Time: {state.time}")
                state = self.step(state)
                if state.scene == Scene.Exiting:
                    break
                state.update_time()
                sleep(self.frame_rate / 100)
            except KeyboardInterrupt:
                print("\nexiting...")
                break
        return state


def main():
    scale = 10
    dimensions = (100, 100)
    frame_rate = 60
    turtle.Screen().setup(scale * 50, scale * 50)
    board = Board(dimensions)
    print(f"apple pos: {board.apple}")
    print(f"snake_head pos: {board.snake.get_head()}")
    drawer = Drawer(scale)
    for i in range(0, 10):
        print(f"Frame {i + 1}")
        drawer.draw_board(board.evaluate_state(Direction.Left)[0])
        drawer.update()
        drawer.clear()
        # sleep(frame_rate * 0.001)

    # drawer.draw_snake_body((0, 0))
    turtle.done()
    # game = Game.initialize((100, 100), 1, 25, keybinds)
    # game.loop()
    # turtle.bye()


if __name__ == "__main__":
    main()
