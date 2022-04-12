import pygame
from game_loop import GameLoop
from renderer import Renderer
from data import GameData


def main():
    width = 700
    height = 600
    display = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Conncet 4")

    renderer = Renderer(display, GameData)
    game_loop = GameLoop(renderer)

    pygame.init()
    game_loop.start()

if __name__ == '__main__':
    main()
