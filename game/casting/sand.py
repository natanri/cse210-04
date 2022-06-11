from game.casting.rock import Rock

class Sand(Rock):

    def __init__(self):
        """
        This will become the player slow and substract 5 points
        """
        super().__init__()
        self._point_value = -5
