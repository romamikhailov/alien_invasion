import pygame

class Ship():
    """A Class to manage a ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its initial position."""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the image of the ship and gets a rectangle.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        # Each new ship appears at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving the real coordinate of the center of the ship.
        self.x = float(self.rect.x)

        # Moving flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship's position based on the flag."""
        # Update the x attribute of the ship object, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect attribute based on self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)