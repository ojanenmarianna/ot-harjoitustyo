import math
import sys
import pygame

from data import GameData
from ui.event_queue import EventQueue
from services.connect_game import ConnectGame


class Renderer:
    """
    Renderer-luokka renderöi näkymät näytölle.
    """
    def __init__(self, start_view, game_view, game_rules_view, new_score_view, score_repository, clock):
        self.game_view = game_view
        self.start_view = start_view
        self.game_rules_view = game_rules_view
        self.new_score_view = new_score_view
        self.score_repository = score_repository
        self.data = GameData()
        self.event_queue = EventQueue()
        self.game = None
        self._clock = clock
        self.game_over = False
        self.turn = 0
        self.winner = None

        self._current_view = None

    def show_start_screen(self):
        """
        Renders the start view screen.
        """
        self._current_view = self.start_view
        self._current_view.render()

        while True:
            if self._handle_start_menu() is False:
                break
            pygame.display.update()

    def show_game_rules(self):
        self._current_view = self.game_rules_view
        self._current_view.render()
        while True:
            if self._handle_start_menu() is False:
                break
            pygame.display.update()

    def show_new_score_screen(self):
        name = self.new_score_view.render(self.winner, self.event_queue)
        self.show_start_screen()
        return name

    def start(self):
        """
        Renderöi pelinäkymän.
        """
        self.game_over = False
        self.turn = 0
        self.game = ConnectGame(self.data, self.game_view)
        self.game.draw()
        self._current_view = self.game_view
        while not self.game_over:
            if self._handle_events() is False:
                break
            pygame.display.flip()
            self._clock.tick(70)
            self.game.draw()
        name = self.show_new_score_screen()
        self.save_new_win(name)

    def save_new_win(self, name):
        self.score_repository.add_new_win(name)

    # event handle tullaan eriyttämään omaksi luokakseen
    def _handle_start_menu(self):
        """
        Käsittelee aloitusnäkymän tapahtumat.
        """
        while True:
            event = self.event_queue.get()
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start()

                if event.key == pygame.K_1:
                    self.show_game_rules()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_r:
                                    return
                            elif event.type == pygame.QUIT:
                                sys.exit()

                if event.key == pygame.K_2:
                    #self.show_high_scores()
                    while True:
                        event = self.event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                            if event.key == pygame.K_d:
                                return "DELETE"
                        elif event.type == pygame.QUIT:
                            sys.exit()

    def _handle_events(self):
        """
        Käsittelee pelin tapahtumat
        """
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.data.sq_size))

                    if self.game.is_valid_location(col):
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col, 1)
                    if self.game.tie_move():
                        self.winner = 0
                        self.game_over = True
                    if self.game.winning_move(1):
                        self.winner = 1
                        self.game_over = True

                    self.turn += 1
                    break

                if self.turn == 1:
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.data.sq_size))

                    if self.game.is_valid_location(col):
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col, 2)
                    if self.game.tie_move():
                        self.winner = 0
                        self.game_over = True
                    if self.game.winning_move(2):
                        self.winner = 2
                        self.game_over = True

                    self.turn -=1
                    break

            elif event.type == pygame.QUIT:
                return False
