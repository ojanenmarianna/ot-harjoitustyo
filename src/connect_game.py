import os
import sys
import pygame

from data import GameData
from renderer import Renderer


class ConnectGame:
    """
    Holds all of the game logic and game data.
    """

    game_data: GameData
    renderer: Renderer

    def __init__(self, game_data: GameData, renderer: Renderer, game_board):
        """
        Initializes the game.
        """
        self.board = game_board
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
        """
        Prints the state of the board to the console
        """
        self.game_data.game_board.print_board()
    
    def is_valid_location(self, col):
        self.game_data.game_board.is_valid_location(col)

    def get_next_open_row(self, col):
        self.game_data.game_board.get_next_open_row(col)

    def drop_piece(self, row, col, piece):
        self.game_data.game_board.drop_piece(row, col, piece)

    def winning_move(self, piece):
        self.game_data.game_board.winning_move(piece)