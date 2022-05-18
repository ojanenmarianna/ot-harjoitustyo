import pygame

from config import black, white, yellow, blue

class TopTenView:
    def __init__(self, screen, width, height, score_repository):
        self._screen = screen
        self._width = width
        self._height = height
        self._score_repository = score_repository

    def render(self):
        self._screen.fill(black)

        text_font = pygame.font.SysFont(None, 48)
        text_content = "TOP 10"
        text = text_font.render(text_content, True, yellow)
        rect = text.get_rect()
        self._screen.blit(text, ((self._width - rect[2])//2, 50))

        text_font = pygame.font.SysFont(None, 36)
        high_scores = self._score_repository.find_top_ten()

        x_axel = 0
        for i in range(10):
            if len(high_scores) - 1 >= i:
                text = text_font.render(
                    str(high_scores[i][0]), True, white)
                self._screen.blit(
                    text, ((self._width - rect[2]*2.5)//2, 150 + x_axel))

                text = text_font.render(
                    str(high_scores[i][1]), True, white)
                self._screen.blit(
                    text, ((self._width + rect[2]*2)//2, 150 + x_axel))
            else:
                text = text_font.render("Player", True, white)
                self._screen.blit(
                    text, ((self._width - rect[2]*2.5)//2, 150 + x_axel))

                text = text_font.render("0", True, white)
                self._screen.blit(
                    text, ((self._width + rect[2]*2)//2, 150 + x_axel))

            x_axel += 50
        
        text_content = "Press 'R' to return"
        text = text_font.render(text_content, True, blue)
        self._screen.blit(text, (100, 600))

        pygame.display.flip()
