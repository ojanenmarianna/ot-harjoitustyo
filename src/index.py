import pygame
from services.game_loop import GameLoop
from ui.game_view import Renderer
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

    renderer = Renderer(display, GameData)
    clock = Clock()
    game_loop = GameLoop(renderer, clock)

    pygame.init()
    game_loop.start()

if __name__ == '__main__':
    main()
