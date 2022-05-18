import sys
import pygame

from config import black, white, yellow


class NewScoreView:
    def __init__(self, screen, width, height, clock):
        self._screen = screen
        self._width = width
        self._height = height
        self._clock = clock

    def render(self, player, event_queue):
        rect = pygame.Rect(self._width//2 - 300,
                           self._height//2 - 200, 600, 400)
        pygame.draw.rect(self._screen, black, rect)

        text_font = pygame.font.SysFont(None, 48)
        if player is None or player == 0:
            text_content = "It's a tie!"
            text = text_font.render(text_content, True, white)
            rect = text.get_rect()
            self._screen.blit(
                text, ((self._width - rect[2])//2, self._height//2 - 150))
        else:
            text_content = "Winner is: Player " + str(player)
            text = text_font.render(text_content, True, white)
            rect = text.get_rect()
            self._screen.blit(
                text, ((self._width - rect[2])//2, self._height//2 - 150))

            text_content = "Type your name"
            text = text_font.render(text_content, True, yellow)
            rect = text.get_rect()
            self._screen.blit(
                text, ((self._width-rect[2])//2, self._height//2 - 100))

        text_content = "Press 'Enter' when you are ready"
        text = text_font.render(text_content, True, white)
        rect = text.get_rect()
        self._screen.blit(
            text, ((self._width-rect[2])//2, self._height//2 + 100))

        text_content = ""
        
        while True:
            name_rect = pygame.Rect(
                self._width//2 - 100, self._height//2 - 15, 200, 30)
            pygame.draw.rect(self._screen, white, name_rect)

            player_input = self.handle_name_input(
                text_content, event_queue)
            if player_input or player_input == "":
                text_content = player_input
            elif player_input is False:
                return text_content

            text = text_font.render(text_content, True, black)
            self._screen.blit(
                text, (self._width//2 - 100, self._height//2 - 15))
            pygame.display.flip()
            self._clock.tick(20)

    def handle_name_input(self, text, event_queue):
        event = event_queue.get()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return False
            if event.key == pygame.K_BACKSPACE:
                if len(text) == 1:
                    return ""
                return text[:len(text)-1]
            else:
                if len(text) == 7:
                    return text
                return text + event.unicode
