from typing import Tuple

from board import GameBoard

class GameData:
    """
    GameData class contains all the data for the Game
    """

    radius: int
    height: int
    width: int
    sq_size: Tuple[int, int]
    game_over: bool
    turn: int
    game_board: GameBoard

    def __init__(self):
        self.game_over = False
        self.turn = 0
        self.last_move_row = []
        self.last_move_col = []
        self.game_board = GameBoard()
        self.action = None

        self.sq_size: int = 100
        self.width: int = 7*self.sq_size
        self.height: int = 6*self.sq_size
        self.size: Tuple[int, int] = (self.width, self.height)
        self.radius: int = int(self.sq_size / 2 - 5)
