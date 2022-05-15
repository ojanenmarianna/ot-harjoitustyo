import pygame

from config import black, blue, red, white

class StartView:
    """
    Piirtää aloitusnäkymän.
    """
    def __init__(self, screen, width, height):
        self._screen = screen
        self._width = width
        self._height = height

    def render(self):
        self._screen.fill(black)

        text_font = pygame.font.SysFont('Corbel', 64)
        text_content = "Connect Four"
        text = text_font.render(text_content, True, blue)
        rect = text.get_rect()
        pygame.draw.rect(
            self._screen, white, ((self._width - rect[2])//2, 130, rect[2], rect[3])
        )
        pygame.display.flip()
        self._screen.blit(text, ((self._width - rect[2])//2, 130))

        pygame.display.flip()

        text_font = pygame.font.SysFont(None, 40)
        text_content = "Press 'enter' to start playing"
        text = text_font.render(
            text_content, True, red)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 300))
        pygame.draw.line(
            self._screen, white, ((self._width - rect[2])//2, 300 + rect[3]), ((self._width + rect[2])//2, 300 + rect[3]))

        text_font = pygame.font.SysFont(None, 36)
        text_content = "Press '1' to see game rules"
        text = text_font.render(text_content, True, red)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 400))
        pygame.draw.line(
            self._screen, white, ((self._width - rect[2])//2, 400 + rect[3]), ((self._width + rect[2])//2, 400 + rect[3]))

        text_content = "Press '2' to see control options"
        text = text_font.render(text_content, True, red)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 450))
        pygame.draw.line(
            self._screen, white, ((self._width - rect[2])//2, 450 + rect[3]), ((self._width + rect[2])//2, 450 + rect[3]))

        text_content = "Press '3' to see high scores"
        text = text_font.render(text_content, True, red)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 500))
        pygame.draw.line(
            self._screen, white, ((self._width - rect[2])//2, 500 + rect[3]), ((self._width + rect[2])//2, 500 + rect[3]))

        pygame.display.flip()