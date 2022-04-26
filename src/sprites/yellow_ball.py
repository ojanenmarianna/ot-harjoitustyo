import pygame
from load_image import load_image

class YellowBall(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = load_image("yellow_ball.png")

        self.rect = self.image.get_rect()

