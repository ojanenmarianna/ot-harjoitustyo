import pygame
from ui.renderer import Renderer
from ui.game_view import GameView
from ui.start_view import StartView
from ui.game_rules_view import GameRulesView
from data import GameData
from clock import Clock


def main():
    game_data = GameData()
    width = 7
    height = 6
    display_height = height * game_data.sq_size
    display_width = width * game_data.sq_size
    display = pygame.display.set_mode((game_data.width, game_data.height))

    pygame.display.set_caption("Connect Four")

    clock = Clock()
    game_view = GameView(display, game_data)
    start_view = StartView(display, display_width, display_height)
    game_rules_view = GameRulesView(display, width, height)
    renderer = Renderer(start_view, game_view, game_rules_view, clock)

    pygame.init()
    renderer.show_start_screen()

if __name__ == '__main__':
    main()
