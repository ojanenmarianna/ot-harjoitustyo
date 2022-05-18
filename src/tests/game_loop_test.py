import unittest
import pygame

from services.game_loop import GameLoop
from data import GameData
from ui.game_view import GameView
from ui.start_view import StartView

class StubClock:
    def tick(self, fps):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        width = 7
        height = 6
        display_height = height * 100
        display_width = width * 100
        display = pygame.display.set_mode((display_width, display_height))

        data = GameData()
        start_view = StartView(display, width, height)
        game_view = GameView(display, data)

        self.game_loop = GameLoop(start_view, game_view, StubClock())

    def test_return(self):
        pass
    