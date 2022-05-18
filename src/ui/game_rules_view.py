import pygame

from config import black, red, white


class GameRulesView:
    def __init__(self, screen, width, height):
        self._screen = screen
        self._width = width
        self._height = height

    def render(self):
        self._screen.fill(black)

        text_font = pygame.font.SysFont(None, 24)
        text_content = "Players drop chips on their turn onto the game board."
        text = text_font.render(text_content, True, white)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 100))

        text_content = "The winner is the one that first gets 4 chips in a row horizontally, vertically or diagonally."
        text = text_font.render(text_content, True, white)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//5, 200))

        text_content = "The game ends when one of the players wins or when the board is full."
        text = text_font.render(text_content, True, white)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//5, 300))

        text_content = "Reference: Wikipedia (2022), https://en.wikipedia.org/wiki/Connect_Four"
        text = text_font.render(text_content, True, white)
        self._screen.blit(text, (50, 400))

        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, red)
        self._screen.blit(text, (10, 500))

        pygame.display.flip()