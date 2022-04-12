import pygame
from data import GameData
from renderer import Renderer
from connect_game import ConnectGame


class GameLoop:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer


    def start(self):
        data = GameData()
        screen = pygame.display.set_mode(data.size)
        game = ConnectGame(data, Renderer(screen, data))

        game.print_board()
        game.draw()

        pygame.display.update()
        pygame.time.wait(10000)

    def _handle_events(self):
        pass

    def _render(self):
        pass