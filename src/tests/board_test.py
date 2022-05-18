import unittest
import numpy as np
from services.board import GameBoard


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.game_board = GameBoard()

    def test_is_valid_location_works_with_valid_location(self):
        bool = self.game_board.is_valid_location(2)
        self.assertEqual(True, bool)

    def test_valid_location_works_with_not_valid_location(self):
        bool = self.game_board.is_valid_location(7)
        self.assertEqual(False, bool)

    def test_piece_drop_works_with_player_one(self):
        self.game_board.drop_piece(0, 1, 1)
        self.assertEqual(1, self.game_board.board[0][1])

    def test_next_open_row_finds_the_next_open_row(self):
        self.game_board.drop_piece(0, 2, 2)
        self.assertEqual(1, self.game_board.get_next_open_row(2))

    def test_get_next_open_row_works_when_there_is_no_open_row(self):
        self.game_board.drop_piece(0, 2, 1)
        self.game_board.drop_piece(1, 2, 1)
        self.game_board.drop_piece(2, 2, 1)
        self.game_board.drop_piece(3, 2, 1)
        self.game_board.drop_piece(4, 2, 1)
        self.game_board.drop_piece(5, 2, 1)
        self.assertEqual(None, self.game_board.get_next_open_row(2))

    def test_check_square_finds_right_color(self):
        self.game_board.drop_piece(0, 1, 1)
        self.assertEqual(True, self.game_board.check_square(1, 0, 1))

    def test_check_square_knows_if_column_is_not_on_board(self):
        self.assertEqual(False, self.game_board.check_square(2, 0, 8))

    def test_check_square_returns_false_if_row_not_oon_board(self):
        self.assertEqual(False, self.game_board.check_square(2, 7, 2))
    def test_is_winning_move_finds_winning_move(self):
        pass

    def test_horizontal_win_finds_horizontal_win(self):
        self.game_board.drop_piece(0, 1, 1)
        self.game_board.drop_piece(0, 2, 1)
        self.game_board.drop_piece(0, 3, 1)
        self.game_board.drop_piece(0, 4, 1)
        self.assertEqual(True, self.game_board.horizontal_win(1, 0, 1))

    def test_winning_move_finds_winning_move(self):
        self.assertEqual(False, self.game_board.winning_move(1))
        self.game_board.drop_piece(0, 1, 1)
        self.game_board.drop_piece(0, 2, 1)
        self.game_board.drop_piece(0, 3, 1)
        self.game_board.drop_piece(0, 4, 1)
        self.assertEqual(True, self.game_board.winning_move(1))

    def test_vertical_win_works_correctly(self):
        self.game_board.drop_piece(0, 1, 1)
        self.game_board.drop_piece(1, 1, 1)
        self.game_board.drop_piece(2, 1, 1)
        self.game_board.drop_piece(3, 1, 1)
        self.assertEqual(True, self.game_board.vertical_win(1, 0, 1))

    def test_tie_move_works_correctly(self):
        self.assertEqual(False, self.game_board.tie_move())
        self.game_board.board = np.ones((6, 7))
        self.assertEqual(True, self.game_board.tie_move())
