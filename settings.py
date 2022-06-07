class Settings():
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes game settings."""

        # Screen settings
        self.screen_widht = 1920
        self.screen_heihgt = 1080
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_widht = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_alowed = 3
