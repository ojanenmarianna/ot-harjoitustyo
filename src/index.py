import pygame
from board import GameBoard


def main():
    pygame.init()

    board = GameBoard()
    board.print_board()
    board.add_token(2,6)
    print("*****************")
    board.print_board()
    # Done! Time to quit.
    pygame.quit()
    

if __name__ == "__main__":
    main()