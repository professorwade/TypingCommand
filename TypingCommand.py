import arcade
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

class TypingCommand(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "TypingCommand")

