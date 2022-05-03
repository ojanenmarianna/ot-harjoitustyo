import sys

from data import GameData
from ui.game_view import GameView


class ConnectGame:
    """
    Holds all of the game logic and game data.
    """

    game_data: GameData
    game_view: GameView

    def __init__(self, game_data: GameData, game_view: GameView, game_board):
        """
        Initializes the game.
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
        Prints the state of the board to the console
        """
        self.game_data.game_board.print_board()

    def is_valid_location(self, col):
        """
        Checks if the mouse is inside the board.
        """
        return self.game_data.game_board.is_valid_location(col)

    def get_next_open_row(self, col):
        """
        Checks if the column has empty rows.
        """
        return self.game_data.game_board.get_next_open_row(col)

    def drop_piece(self, row, col, piece):
        """
        Drops the chip into the right location.
        """
        self.game_data.game_board.drop_piece(row, col, piece)

    def winning_move(self, piece):
        """
        Checks if the player has 4 chips on a row the board.
        """
        return self.game_data.game_board.winning_move(piece)

    def tie_move(self):
        """
        Checks if the board is full of chips.
        """
        return self.game_data.game_board.tie_move()
