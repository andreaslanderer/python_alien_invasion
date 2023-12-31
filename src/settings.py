class Settings:
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1_200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # (light shade of gray)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # (dark shade of gray)
        self.bullets_allowed = 3

    def get_display_mode(self):
        return self.screen_width, self.screen_height

