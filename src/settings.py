class Settings:
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1_200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # (light shade of gray)

    def get_display_mode(self):
        return self.screen_width, self.screen_height

