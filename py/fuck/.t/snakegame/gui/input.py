# def register_keybinds():

from dataclasses import dataclass
from enum import Enum, auto

# from turtle import Screen
import pygame
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
                raise ValueError("cannot convert PlayPause key to Direction")
            case self.Null:
                raise ValueError("cannot convert Null key to Direction")


class Input:
    def __init__(self, keybindings: dict[str, Key]):
        self.last_pressed: Key = Key.Null
        self.event = pygame.event
        # for key_str, key in keybindings.items():
        # screen.onkeypress(lambda: self.set_input(key), key_str)

    def reset_pressed(self):
        self.last_pressed = Key.Null

    def get_input(self) -> Key:
        # figure out how to just pop the event pump
        match self.event.get()[0]:
            case pygame.QUIT:
                return Key.Exit
            case _:
                return self.last_pressed

    def set_input(self, key: Key):
        self.last_pressed = key
