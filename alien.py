import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent an alien"""

    def __init__(self, ai_game):
        """Initialize the alien and set its the initial position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien image and gets the rectangle.
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.x = self.rect.height

        # Save the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien left and right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

