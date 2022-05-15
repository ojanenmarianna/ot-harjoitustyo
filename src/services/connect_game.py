import sys

from data import GameData
from ui.game_view import GameView


class ConnectGame:
    """
    Sisältää pelin logiikan ja datan.
    """

    game_data: GameData
    game_view: GameView

    def __init__(self, game_data: GameData, game_view: GameView, game_board):
        """
        Alustaa pelin.
        """
        self.board = game_board
        self.game_data = game_data
        self.game_view = game_view

    def quit(self):
        sys.exit()

    def draw(self):
        self.game_view.draw(self.game_data)

    def print_board(self):
        """
        Printtaa laudan tilanteen konsoliin.
        """
        self.game_data.game_board.print_board()

    def is_valid_location(self, col):
        """
        Tarkistaa, onko hiiri laudan sisällä.
        """
        return self.game_data.game_board.is_valid_location(col)

    def get_next_open_row(self, col):
        """
        Tarkistaa, onko kolumnilla tyhjiä rivejä.
        """
        return self.game_data.game_board.get_next_open_row(col)

    def drop_piece(self, row, col, piece):
        """
        Tiputtaa pelimerkin oikeaan paikkaan.
        """
        self.game_data.game_board.drop_piece(row, col, piece)

    def winning_move(self, piece):
        """
        Tarkistaa, onko pelaajalla 4 merkkiä peräkkäin pelilaudalla.
        """
        return self.game_data.game_board.winning_move(piece)

    def tie_move(self):
        """
        Tarkistaa, onko peliluta täynnä.
        """
        return self.game_data.game_board.tie_move()
