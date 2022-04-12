from lib2to3.pygram import python_grammar_no_print_statement


import pygame
import os


class ImageLoader():

    def __init__(self, filename):        
        self.dirname = os.path.dirname(__file__)
        self.filename = filename


    def load_image(self):
        return pygame.image.load(os.path.join(self.dirname, "assets", self.filename))
