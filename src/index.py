import pygame
from services.game_loop import GameLoop
from ui.game_view import GameData, GameView
from data import GameData
from clock import Clock
from ui.start_view import StartView

CELL_SIZE = 100

def main():
    width = 7
    height = 6
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Connect Four")

    game_view = GameView(display, GameData)
    start_view = StartView(display, display_width, display_height)
    clock = Clock()
    game_loop = GameLoop(start_view, game_view, clock)

    pygame.init()
    game_loop.start_screen()

if __name__ == '__main__':
    main()
