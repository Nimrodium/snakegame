# def register_keybinds():

from dataclasses import dataclass
from enum import Enum, auto

# from turtle import Screen
import pygame
from pygame.event import Event

from engine.shared import Direction


class Key(Enum):
    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()
    Exit = auto()
    Null = auto()
    PlayPause = auto()

    def to_direction(self) -> Direction:
        """converts a key into a direction; will error on Exit,Null"""
        match self:
            case self.Up:
                return Direction.Up
            case self.Down:
                return Direction.Down
            case self.Left:
                return Direction.Left
            case self.Right:
                return Direction.Right
            case self.Exit:
                raise ValueError("cannot convert Exit key to Direction")
            case self.PlayPause:
                return Direction.Last
            case self.Null:
                return Direction.Last


class Input:
    def __init__(self, keybindings: dict[int, Key]):
        # self.last_pressed: Key = Key.Null
        # self.event = pygame.event
        self.keybindings = keybindings
        # for key_str, key in keybindings.items():
        # screen.onkeypress(lambda: self.set_input(key), key_str)

    # def reset_pressed(self):
    #     self.last_pressed = Key.Null

    def get_input(self) -> Key:
        pygame.event.pump()
        pressed_keys = pygame.key.get_pressed()
        space = pressed_keys[pygame.K_SPACE]
        print(f"space={space}; {pygame.K_SPACE}; {self.keybindings[pygame.K_SPACE]}")
        # honestly vile
        # print(pygame.key.get_pressed())
        print(f"space = {self.keybindings[pygame.K_SPACE]}; {pygame.K_SPACE}")
        # pressed_valid_keys = filter(
        #     # lambda x: x[0] in self.keybindings.keys(),
        #     lambda x: True,
        #     filter(lambda x: x[1], enumerate(pygame.key.get_pressed())),
        # )
        pressed_valid_keys = filter(
            lambda k: k[1],
            map(lambda k: (k, pressed_keys[k]), self.keybindings.keys()),
        )

        try:
            key = self.keybindings[next(pressed_valid_keys)[0]]
            print(f"pressed keys = {list(pressed_valid_keys)}; key={key}")
            return key
        except StopIteration:
            return Key.Null

        # event: Event
        # while True:
        #     ev = pygame.event.poll()
        #     if ev.type == pygame.KEYDOWN:
        #         event = ev
        #         break
        # print(event)
        # key: Key
        # if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
        #     if event.key in self.keybindings.keys():
        #         key = self.keybindings[event.key]
        #         self.last_pressed = key
        #         return key
        #     else:
        #         key = self.last_pressed
        #         return key
        # else:
        #     return self.last_pressed

        # if event.mod == pygame.KMOD_NONE:

        # key = pygame.key.get_pressed()
        # figure out how to just pop the event pump
        # event = self.event.poll()
        # if event == pygame.KEYDOWN
        # key: Key
        # match event:
        #     case pygame.QUIT:
        #         key = Key.Exit
        #     case pygame.NOEVENT:
        #         key = Key.Null
        #     case ev if ev.key in self.keybindings.values():
        #         key = self.keybindings[ev.key]
        #     case _:
        #         key = self.last_pressed
        # self.last_pressed = key
        # return key

    # def set_input(self, key: Key):
    #     self.last_pressed = key
