from game.casting.artifact import Artifact

class Gem(Artifact):

    """
    This will increase the score point when it collected
    """

    def __init__(self):
        super().__init__()
        self._point_value = 1
        

    def get_point_value(self):
        #This will return amount of points added to the score

        return self._point_value


