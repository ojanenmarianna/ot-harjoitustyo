import pygame
import math
from data import GameData
from renderer import Renderer
from connect_game import ConnectGame
from board import GameBoard


class GameLoop:
    def __init__(self, renderer: Renderer):
        self._renderer = renderer
        self.data = GameData()
        self.game = None
        self.game_over = False
        self.turn = 0


    def start(self):
        screen = pygame.display.set_mode(self.data.size)
        self.game = ConnectGame(self.data, Renderer(screen, self.data), GameBoard)

        self.game.draw()

        while True:
            if self._handle_events()  == False:
                break
            self.turn += 1
            self.turn = self.turn % 2 
            #self.game.print_board()
            self.game.update()
            self._render()
            self.game.draw()

    def _render(self):
        self._renderer.render()
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.data.sq_size))
                    print(col)

                    if self.game.is_valid_location(col) != 0:
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col, 1)
                        print("valid")

                        if self.game.winning_move(1):
                            print("Player 1 wins!")
                            self.game_over = True

                if self.turn == 1:
                    posx = event.pos[0]
                    col = int(math.floor(posx/self.data.sq_size))

                    if self.game.is_valid_location(col):
                        row = self.game.get_next_open_row(col)
                        self.game.drop_piece(row, col, 2)

                        if self.game.winning_move(2):
                            print("Player 2 wins!")
                            self.game_over = True
            elif event.type == pygame.QUIT:
                return False