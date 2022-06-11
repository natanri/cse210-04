from game.casting.actors import Actor
from game.shared.point import Point

from game.shared.color import Color

import random



class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def move_down(self):
        y = self._position.get_y() + 5

        if y == 600:
            y = 0

        y = self._position = Point(self._position.get_x(), y)

    def refresh(self):
        x = random.randint(1, 59)

        position = Point(x, 0)
        position = position.scale(15)
        self.set_position(position)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.set_color(Color(r, g, b))

