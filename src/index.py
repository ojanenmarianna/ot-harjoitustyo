import pygame
from ui.renderer import Renderer
from ui.game_view import GameView
from ui.start_view import StartView
from ui.game_rules_view import GameRulesView
from ui.new_score_view import NewScoreView
from ui.top_ten_view import TopTenView
from data import GameData
from clock import Clock
from repositories.score_repository import (
    score_repository as default_score_repository)


def main():
    game_data = GameData()
    width = 7
    height = 6
    display_height = height * game_data.sq_size
    display_width = width * game_data.sq_size
    display = pygame.display.set_mode((game_data.width, game_data.height))

    pygame.display.set_caption("Connect Four")

    clock = Clock()
    score_repository = default_score_repository
    game_view = GameView(display, game_data)
    start_view = StartView(display, display_width, display_height)
    game_rules_view = GameRulesView(display, display_width, display_height)
    new_score_view = NewScoreView(display, display_width, display_height, clock)
    top_ten_view = TopTenView(display, display_width, display_height, default_score_repository)
    renderer = Renderer(start_view, game_view, game_rules_view,
                        new_score_view, top_ten_view, score_repository, clock)

    pygame.init()
    renderer.show_start_screen()

if __name__ == '__main__':
    main()
