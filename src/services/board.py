import numpy as np


class GameBoard():
    """ GameBoard class holds the state of the game board
    and methods to manipulate and query the board.
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
        return self.board[self.rows-1][col] == 0

    def get_next_open_row(self, col):
        for row in range(self.rows - 1):
            if self.board[row][col] == 0:
                return row

        return self.tie_move()

    def check_square(self, piece, row, col):
        """
        Checks if a particular square is a certain color.  If
        the space is off of the board it returns False.

        :param piece: The piece color to look for.
        :param row: The row to check.
        :param col: The column to check.

        :return: Whether the square is on the board and has the color/piece specified.
        """
        if row < 0 or row >= self.rows:
            return False

        if col < 0 or col >= self.cols:
            return False

        return self.board[row][col] == piece

    def horizontal_win(self, piece, row, col):
        """
        Checks if there is a horizontal win at the position (row, col).

        :param piece: The color of the chip to check for.
        :param row: The row.
        :param col: The column.

        :return: Whether there is a horizontal win at the position (row, col).
        """
        return (
            self.check_square(piece, row, col)
            and self.check_square(piece, row, col + 1)
            and self.check_square(piece, row, col + 2)
            and self.check_square(piece, row, col + 3)
        )

    def vertical_win(self, piece, row, col):
        """
        Checks if there is vertical win at the position (row, col)
        :param piece: The color of the chip to check for.

        :param row: The row
        :param col: The column

        :return: Whether there is a vertical win at the position (row, col)
        """
        return (
            self.check_square(piece, row, col)
            and self.check_square(piece, row + 1, col)
            and self.check_square(piece, row + 2, col)
            and self.check_square(piece, row + 3, col)
        )

    def diagonal_win(self, piece, row, col):
        """
        Checks if there is a diagonal_win at the position (row, col)
        :param piece: The color of the chip to check for.

        :param row: The row
        :param col: The column

        :return: Whether there is a diagonal win at the position (row, col)
        """
        return (
            self.check_square(piece, row, col)
            and self.check_square(piece, row + 1, col + 1)
            and self.check_square(piece, row + 2, col + 2)
            and self.check_square(piece, row + 3, col + 3)
        ) or (
            self.check_square(piece, row, col)
            and self.check_square(piece, row - 1, col + 1)
            and self.check_square(piece, row - 2, col + 2)
            and self.check_square(piece, row - 3, col + 3)
        )

    def winning_move(self, piece):
        """
        Checks if the current piece has won the game.

        :param piece: The color of the chip to check for.
        :return: Whether the current piece has won the game.
        """
        for col in range(self.cols):
            for row in range(self.rows):
                if (
                    self.horizontal_win(piece, row, col)
                    or self.vertical_win(piece, row, col)
                    or self.diagonal_win(piece, row, col)
                ):
                    return True
        return False

    def tie_move(self):
        """
        Checks for a tie game.

        :return:  Whether a tie has occurred.
        """
        slots_filled: int = 0

        for col in range(self.cols):
            for row in range(self.rows):
                if self.board[row][col] != 0:
                    slots_filled += 1

        return slots_filled == 35
