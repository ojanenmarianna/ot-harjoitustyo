#import pygame
import numpy as np


class GameBoard():
    """ GameBoard class holds the state of the game board
    and methods to manipulate and query the board
    """

    def __init__(self):
        """
        Initializes the game board
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

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, col):
        return True
        #return self.board[self.rows-1][col] == 0
    
    def get_next_open_row(self, col):
        for row in range(self.rows):
            if self.board[row][col] == 0:
                return row

    def winning_move(self, piece):
        for col in range(self.cols - 3):
            for row in range(self.rows):
                if self.board[row][col] == piece and self.board[row][col + 1] == piece and self.board[row][col + 2] and self.board[row][col + 3] == piece:
                    return True

        for col in range(self.cols):
            for row in range(self.rows):
                if self.board[row][col] == piece and self.board[row+1][col] == piece and self.board[row+2][col] == piece and self.board[row+3][col] == piece:
                    return True
