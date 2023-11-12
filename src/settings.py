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
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # (dark shade of gray)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def get_display_mode(self):
        return self.screen_width, self.screen_height

