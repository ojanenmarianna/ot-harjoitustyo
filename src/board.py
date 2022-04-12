#import pygame
import numpy as np


class GameBoard():
    """ GameBoard class holds the state of the game board,so
    and methods to manipulate and query the board
    """

    def __init__(self):
        """
        Initializes the game Board
        """
        self.rows = 6
        self.cols = 7
        self.board = np.zeros((self.rows, self.cols))

        self.print_board()

    def print_board(self):
        """ 
        Prints the state of the board to the console
        """
        print(np.flip(self.board, 0))
        print("-----------------------")
        print(" " + str([1, 2, 3, 4, 5, 6, 7]))