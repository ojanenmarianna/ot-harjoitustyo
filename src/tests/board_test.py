import unittest
import numpy as np
import pygame
from data import GameData
from ui.game_view import GameView
from services.connect_game import ConnectGame


class TestBoard(unittest.TestCase):
    def setUp(self):
        width = 7
        height = 6
        display_height = height * 100
        display_width = width * 100
        display = pygame.display.set_mode((display_width, display_height))

        data = GameData
        view = GameView(display, data)
        self.game = ConnectGame(data, view)

    def test_is_valid_location_works_with_valid_location(self):
        bool = self.game.is_valid_location(2)
        self.assertEqual(True, bool)

    def test_valid_location_works_with_not_valid_location(self):
        bool = self.game.is_valid_location(7)
        self.assertEqual(False, bool)

    def test_piece_drop_works_with_player_one(self):
        self.game.drop_piece(0, 1, 1)
        self.assertEqual(1, self.game.board.board[0][1])

    def test_next_open_row_finds_the_next_open_row(self):
        self.game.drop_piece(0, 2, 2)
        self.assertEqual(1, self.game.get_next_open_row(2))

    def test_get_next_open_row_works_when_there_is_no_open_row(self):
        self.game.drop_piece(0, 2, 1)
        self.game.drop_piece(1, 2, 1)
        self.game.drop_piece(2, 2, 1)
        self.game.drop_piece(3, 2, 1)
        self.game.drop_piece(4, 2, 1)
        self.game.drop_piece(5, 2, 1)
        self.assertEqual(None, self.game.get_next_open_row(2))

    def test_check_square_finds_right_color(self):
        self.game.drop_piece(0, 1, 1)
        self.assertEqual(True, self.game.check_square(1, 0, 1))

    def test_check_square_knows_if_column_is_not_on_board(self):
        self.assertEqual(False, self.game.check_square(2, 0, 8))

    def test_check_square_returns_false_if_row_not_oon_board(self):
        self.assertEqual(False, self.game.check_square(2, 7, 2))
    def test_is_winning_move_finds_winning_move(self):
        pass

    def test_horizontal_win_finds_horizontal_win(self):
        self.game.drop_piece(0, 1, 1)
        self.game.drop_piece(0, 2, 1)
        self.game.drop_piece(0, 3, 1)
        self.game.drop_piece(0, 4, 1)
        self.assertEqual(True, self.game.horizontal_win(1, 0, 1))

    def test_winning_move_finds_winning_move(self):
        self.assertEqual(False, self.game.winning_move(1))
        self.game.drop_piece(0, 1, 1)
        self.game.drop_piece(0, 2, 1)
        self.game.drop_piece(0, 3, 1)
        self.game.drop_piece(0, 4, 1)
        self.assertEqual(True, self.game.winning_move(1))

    def test_vertical_win_works_correctly(self):
        self.game.drop_piece(0, 1, 1)
        self.game.drop_piece(1, 1, 1)
        self.game.drop_piece(2, 1, 1)
        self.game.drop_piece(3, 1, 1)
        self.assertEqual(True, self.game.vertical_win(1, 0, 1))

    def test_tie_move_works_correctly(self):
        self.assertEqual(False, self.game.tie_move())
        self.game.board.board = np.ones((6, 7))
        self.assertEqual(True, self.game.tie_move())
