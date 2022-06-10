class Settings():
    """A class for storing all Alien Invasion game settings."""

    def __init__(self):
        """Initializes game settings."""

        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 means moving to the right; and -1 - to the left.
        self.fleet_direction = 1
