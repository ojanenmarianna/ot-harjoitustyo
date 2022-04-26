import pygame
from game_loop import GameLoop
from renderer import Renderer
from data import GameData

CELL_SIZE = 100

def main():
    width = 7
    height = 6
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("Connect Four")

    renderer = Renderer(display, GameData)
    game_loop = GameLoop(renderer)

    pygame.init()
    game_loop.start()

if __name__ == '__main__':
    main()
