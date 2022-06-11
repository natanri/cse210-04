from game.casting.artifact import Artifact

class Rock(Artifact):
    """
    This class inheritate atrributes from Artifact class but this will damage the player and subtract point from it
    """

    def __init__(self):
        super().__init__()
        self._point_value = -1

    def get_point_value(self):
        """
        It will subtract a certain amount of points.
        """

        return self._point_value
