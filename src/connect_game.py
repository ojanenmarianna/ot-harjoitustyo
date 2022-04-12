import math
import os
import sys
import pygame
from data import GameData
from board import GameBoard
from renderer import Renderer


class ConnectGame:
    """
    This class holds all of the game logic and game data.
    """

    game_data: GameData
    renderer: Renderer

    def __init__(self, game_data: GameData, renderer: Renderer):
        """
        Initializes the game.
        """
        self.game_data = game_data
        self.renderer = renderer

    def quit(self):
        sys.exit()

    def update(self):
        if self.game_data.game_over:
            print(os.getpgid())
            pygame.time.wait(1000)
            os.system("game_loop.py")

    def draw(self):
        self.renderer.draw(self.game_data)

    def print_board(self):
        self.game_data.game_board.print_board()