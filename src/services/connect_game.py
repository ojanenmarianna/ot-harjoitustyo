import sys

from data import GameData
from ui.game_view import GameView
from services.board import GameBoard


class ConnectGame:
    """
    Sisältää pelin logiikan ja datan.
    """

    game_data: GameData
    game_view: GameView

    def __init__(self, game_data: GameData, game_view: GameView):
        """
        Alustaa pelin.
        """
        self.rows = 6
        self.cols = 7
        self.board = GameBoard()
        self.game_data = game_data
        self.game_view = game_view

    def quit(self):
        sys.exit()

    def draw(self):
        self.game_view.draw_board(self.board)

    def is_valid_location(self, col):
        """
        Tarkistaa, onko hiiri laudan sisällä.
        """
        if col >= self.cols or col < 0:
            return False
        return self.board.board[self.rows-1][col] == 0

    def get_next_open_row(self, col):
        """
        Tarkistaa, onko kolumnilla tyhjiä rivejä.
        """
        for row in range(self.rows - 1):
            if self.board.board[row][col] == 0:
                return row

    def drop_piece(self, row, col, piece):
        """
        Tiputtaa pelimerkin oikeaan paikkaan.
        """
        self.board.board[row][col] = piece

    def check_square(self, piece, row, col):
        """
        Tarkistaa, onko tietty ruutu tietyn värinen. Jos tila
        on laudan ulkopuolelta, palauttaa False.

        :param piece: Väri, jota etsitään.
        :param row: Rivi, joka tarkistetaan.
        :param col: Kolumni, joka tarkistetaan.

        :return: Onko ruutu laudalla, onko ruutu sitä väriä, jota etsitään.
        """
        if row < 0 or row >= self.rows:
            return False

        if col < 0 or col >= self.cols:
            return False

        return self.board.board[row][col] == piece

    def horizontal_win(self, piece, row, col):
        """
        Tarkistaa horisontaalisen voiton.

        :param piece: Merkin väri, jota tarkistetaan.
        :param row: Rivi, josta tarkistetaan.
        :param col: Kolumni, josta atarkistetaan

        :return: Onko laudalla horisontaalinen voitto.
        """
        return (
            self.check_square(piece, row, col)
            and self.check_square(piece, row, col + 1)
            and self.check_square(piece, row, col + 2)
            and self.check_square(piece, row, col + 3)
        )

    def vertical_win(self, piece, row, col):
        """
        CTarkistaa, onko laudalla vertikaalinen voitto.
        :param piece: Merkin väri, jota tarkistetaan.

        :param row: Rivi, jota tarkistetaan.
        :param col: Kolumni,jota tarkistetaan.

        :return: Onko laudalla vertikaalinen voitto.
        """
        return (
            self.check_square(piece, row, col)
            and self.check_square(piece, row + 1, col)
            and self.check_square(piece, row + 2, col)
            and self.check_square(piece, row + 3, col)
        )

    def diagonal_win(self, piece, row, col):
        """
        Tarkistaa, onko laudala diagonaalinen voitto.
        :param piece: Merkin väri, jota tarkistetaan.

        :param row: Rivi, jota tarkitetaan
        :param col: Kolumni, jota tarkistetaan.

        :return: Onko laudalla diagonaalinn voitto.
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
        Tarkistaa, voittaako nykyisellä merkillä pelin.

        :param piece: Väri (pelaaja), jonka voitto tarkistetaan.
        :return: Voittaako nykyinen merkki pelin.
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
        Tarkastaa, päättyykö peli tasan.

        :return:  Onko peli päättynyt tasan.
        """
        slots_filled: int = 0

        for col in range(self.cols):
            for row in range(self.rows):
                if self.board.board[row][col] != 0:
                    slots_filled += 1

        return slots_filled >= 35
