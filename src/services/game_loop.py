import math
import pygame

from data import GameData
from ui.game_view import GameView
from ui.start_view import StartView
from ui.event_queue import EventQueue
from services.connect_game import ConnectGame
from services.board import GameBoard


class GameLoop:
    """
    GameLoop luokka renderöi näkymät näytölle.
    """
    def __init__(self, start_view: StartView, game_view: GameView, clock):
        self.game_view = game_view
        self.start_view = start_view
        self.data = GameData()
        self.event_queue = EventQueue()
        self.game = None
        self._clock = clock
        self.game_over = False
        self.turn = 0

        self._current_view = None

    def show_start_screen(self):
        """
        Renders the start view screen.
        """
        self._current_view = self.start_view
        self._current_view.render()
        running = True
        while running:
            if self._handle_start_menu() is False:
                break
            pygame.display.update()
            self._clock.tick(1)



    def start(self):
        """
        Renderöi pelinäkymän.
        """
        screen = pygame.display.set_mode(self.data.size)
        game_view = GameView(screen, self.data)
        self.game = ConnectGame(self.data, game_view)
        self.game.draw()
        self._current_view = game_view
        while not self.game_over:
            if self._handle_events() is False:
                break
            pygame.display.flip()
            self._clock.tick(70)
            self.game.draw()

    def show_pause(self):
        '''Näyttää pause-näytön
        '''
        self._current_view.pause()
        self._clock.tick(1)

    # event handle tullaan eriyttämään omaksi luokakseen
    def _handle_start_menu(self):
        """
        Käsittelee aloitusnäkymän tapahtumat.
        """
        while True:
            event = self.event_queue.get()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start()

                if event.key == pygame.K_1:
                    #renderer.show_game_rules()
                    while True:
                        event = self.event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                        elif event.type == pygame.QUIT:
                            self.game.quit()

                if event.key == pygame.K_2:
                    #renderer.show_control_options()
                    while True:
                        event = self.event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                        elif event.type == pygame.QUIT:
                            self.game.quit()

                if event.key == pygame.K_3:
                    #renderer.show_high_scores()
                    while True:
                        event = self.event_queue.get()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                return
                            if event.key == pygame.K_d:
                                return "DELETE"
                        elif event.type == pygame.QUIT:
                            self.game.quit()

            if event.type == pygame.KEYDOWN:
                self.start()

            if event.type == pygame.QUIT:
                return False

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
                        print("It's a tie!")
                        self.game_over = True

                    if self.game.winning_move(1):
                        print("Player 1 wins!")
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
                        print("It's a tie!")
                        self.game_over = True

                    if self.game.winning_move(2):
                        print("Player 2 wins!")
                        self.game_over = True

                    self.turn -=1
                    break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    while True:
                        self.show_pause()
                        if event.type == pygame.QUIT:
                            self.game.quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                self.game.draw()
                                break

            elif event.type == pygame.QUIT:
                return False
