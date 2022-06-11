from game.casting.gems import Gem

class Silver(Gem):
    """
    This will give velocity to the player for a brief moment
    """

    def __init__(self):
        super().__init__()
        self._point_value = 2
