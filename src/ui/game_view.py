# pylint: disable=invalid-name
import pygame
from pygame.gfxdraw import aacircle, filled_circle

from assets.assets import red_chip, yellow_chip, black_chip
from config import blue, black
from data import GameData

class GameView:
    def __init__(self, screen, data: GameData):
        """
        Initializes the game renderer.
        """
        self.red_chip = red_chip
        self.yellow_chip = yellow_chip
        self.black_chip = black_chip

        self.screen = screen
        self.game_data = data

        pygame.display.flip()

    def draw_red_chip(self, x, y):
        """
        Draws a red chip.
        """
        self.screen.blit(self.red_chip, (x, y))

    def draw_yellow_chip(self, x, y):
        """
        Draws a yellow chip.
        """
        self.screen.blit(self.yellow_chip, (x, y))

    def draw_black_chip(self, x, y):
        """
        Draws a black chip.
        """
        self.screen.blit(self.black_chip, (x, y))

    def draw_coin(self, game_data, x, y):
        """
        Draws a coin to the specified position
        using the color of the current player.
        """
        if game_data.turn == 0:
            self.screen.blit(self.red_chip, (x, y))
        else:
            self.screen.blit(self.yellow_chip, (x, y))


    def draw(self, game_data: GameData):
        """
        Draws the game state, including the board and the pieces.
        """
        if game_data.action == "undo":
            filled_circle(
                self.screen,
                game_data.last_move_row,
                game_data.last_move_col,
                self.game_data.radius,
                black,
            )

            aacircle(
                self.screen,
                game_data.last_move_row,
                game_data.last_move_col,
                self.game_data.radius,
                black,
            )

            self.draw_black_chip(
                game_data.last_move_col * self.game_data.sq_size + 5,
                self.game_data.height
                - (
                    game_data.last_move_row * self.game_data.sq_size
                    + self.game_data.sq_size
                    - 5
                ),
            )

            game_data.game_board.print_board()
            game_data.action = None

        self.draw_board(game_data.game_board)

    def draw_board(self, board):
        """
        Draws the game board to the screen.
        :param board: The game board.
        """
        sq_size = self.game_data.sq_size
        height = self.game_data.height
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

        for col in range(board.cols):
            for row in range(board.rows):
                if board.board[row][col] == 1:
                    self.draw_red_chip(
                        int(col * sq_size) + 5, height - int(row * sq_size + sq_size - 5)
                    )

                elif board.board[row][col] == 2:
                    self.draw_yellow_chip(
                        int(col * sq_size) + 5, height - int(row * sq_size + sq_size - 5)
                    )

        pygame.display.flip()
