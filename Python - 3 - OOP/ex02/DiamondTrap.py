from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """The mad King himself"""

    def __init__(self, first_name):
        """
        Constructor for the King class.
        Inherits from Baratheon and Lannister
        """
        super().__init__(first_name)

    @property
    def eyes(self):
        """Get the color of the eyes"""
        return self.eyes

    @eyes.setter
    def eyes(self, color):
        """Set the color of the eyes"""
        self.eyes = color

    @property
    def hairs(self):
        """Get the color of the hairs"""
        return self.hairs

    @hairs.setter
    def hairs(self, color):
        """Set the color of the hairs"""
        self.hairs = color
