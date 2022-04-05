import pygame

class GameBoard():
    def __init__(self):
        #empty board
        self.columns = 7
        self.rows = 7
        self.board = []
        for i in range(self.rows):
            self.board.append([])
            for j in range(self.columns):
                self.board[i].append(0)


    def print_board(self):
        for column in range(len(self.board)):
            for row in range(self.rows):
                print(self.board[column][row],end = ' ')
            print('\n')

    def add_token(self,x,y):
        self.board[x][y] = 1