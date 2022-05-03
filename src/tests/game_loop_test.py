import unittest
import pygame

from services.game_loop import GameLoop

class StubRenderer:
    def render(self):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        pass
    