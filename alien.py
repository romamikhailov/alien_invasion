import pygame
from pygame import Sprite

class Alien(Sprite):
    """A class to manage a alien"""

    def __init__(self):
        """Initialize the alien and set its the initial position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and gets the rectangle.
        self.image = pygame.image.load('images/alien.jpg')