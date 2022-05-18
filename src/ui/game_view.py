# pylint: disable=invalid-name
import pygame
from pygame.gfxdraw import aacircle, filled_circle

from assets.assets import red_chip, yellow_chip, black_chip
from config import blue, black, red, white
from data import GameData

class GameView:
    """
    Sisältää logiikan pelinäkymän renderöintiin.
    """
    def __init__(self, screen, data: GameData):
        """
        Alustaa pelinäkymän.
        """
        self.red_chip = red_chip
        self.yellow_chip = yellow_chip
        self.black_chip = black_chip

        self.screen = screen
        self.game_data = data

        pygame.display.flip()

    def draw_red_chip(self, x, y):
        self.screen.blit(self.red_chip, (x, y))

    def draw_yellow_chip(self, x, y):
        self.screen.blit(self.yellow_chip, (x, y))

    def draw_black_chip(self, x, y):
        self.screen.blit(self.black_chip, (x, y))

    def draw_coin(self, game_data, x, y):
        """
        Piirtää pelimerkin tiettyyn paikkaan käyttäen
        nykyisen pelaajan väriä.
        """
        if game_data.turn == 0:
            self.screen.blit(self.red_chip, (x, y))
        else:
            self.screen.blit(self.yellow_chip, (x, y))


    def draw(self, game_board):
        """
        Piirtää pelin tilan, mukaan lukien laudan ja merkit.
        """
        if self.game_data.action == "undo":
            filled_circle(
                self.screen,
                self.game_data.last_move_row,
                self.game_data.last_move_col,
                self.game_data.radius,
                black,
            )

            aacircle(
                self.screen,
                self.game_data.last_move_row,
                self.game_data.last_move_col,
                self.game_data.radius,
                black,
            )

            self.draw_black_chip(
                self.game_data.last_move_col * self.game_data.sq_size + 5,
                self.game_data.height
                - (
                    self.game_data.last_move_row * self.game_data.sq_size
                    + self.game_data.sq_size
                    - 5
                ),
            )

            self.game_data.action = None

        self.draw_board(game_board)

    def draw_board(self, board):
        """
        Piirtää pelilaudan näytölle.

        :param board: Pelilauta
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

    def pause(self):
        self.screen.fill(black)
        pygame.display.flip()
        text_font = pygame.font.SysFont("Corbel", 48)
        text_content = "Paused"
        text = text_font.render(text_content, True, white)

        self.screen.blit(text, (200, 200))

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Press 'P' to continue"
        text = text_font.render(text_content, True, red)

        self.screen.blit(text, (260, 350))
        pygame.display.flip()