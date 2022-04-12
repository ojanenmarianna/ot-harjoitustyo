import pygame
from pygame.gfxdraw import aacircle, filled_circle
from config import blue, black
from data import GameData

class Renderer:
    def __init__(self, screen, data: GameData):
        """
        Initializes the game renderer.pygame
        """
        self.screen = screen
        self.game_data = data

        self.render()

    def render(self):
        pygame.display.update()

    def draw(self, game_data: GameData):
        """
        Draws the game state, including the board and the pieces.
        """
        game_data.game_board.print_board()
        game_data.action = None

        self.draw_board(game_data.game_board)

    def draw_board(self, board):
        """
        Draws the game board to the screen.
        :param board: The game board.
        """
        sq_size = 100
        radius = int(sq_size / 2 - 5)

        for col in range(board.cols):
            for row in range(board.rows):
                pygame.draw.rect(
                    self.screen,
                    blue,
                    (col * sq_size, (row + 1) * sq_size, sq_size, sq_size),
                )
                aacircle(
                    self.screen,
                    int(col * sq_size + sq_size / 2),
                    int((row + 1) * sq_size + sq_size / 2),
                    radius,
                    black,
                )
                filled_circle(
                    self.screen,
                    int(col * sq_size + sq_size / 2),
                    int((row + 1) * sq_size + sq_size / 2),
                    radius,
                    black,
                )

        pygame.display.update()
