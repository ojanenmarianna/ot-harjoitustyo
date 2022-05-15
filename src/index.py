import pygame
from services.game_loop import GameLoop
from ui.game_view import GameView
from ui.start_view import StartView
from data import GameData
from clock import Clock

CELL_SIZE = 100

def main():
    width = 7
    height = 6
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Connect Four")

    clock = Clock()
    game_view = GameView(display, GameData)
    start_view = StartView(display, display_width, display_height)

    game_loop = GameLoop(start_view, game_view, clock)

    pygame.init()
    game_loop.show_start_screen()

if __name__ == '__main__':
    main()
