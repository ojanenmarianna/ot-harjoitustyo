import numpy as np


class GameBoard():
    """ GameBoard class holds the state of the game board
    and methods to manipulate and query the board.
    """

    def __init__(self):
        """
        Alustaa pelilaudan.
        """
        self.rows = 6
        self.cols = 7
        self.board = np.zeros((self.rows, self.cols))
