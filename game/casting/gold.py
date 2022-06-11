from game.casting.gems import Gem

class Gold(Gem):

    def __init__(self):
        """
        A gold is a special material that will give more points to our player
        """
        super().__init__()
        self._point_value = 5
