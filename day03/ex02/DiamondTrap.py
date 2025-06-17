from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class inheriting from Baratheon and Lannister"""

    def set_eyes(self, color):
        """Set the eye color (King)"""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hair color (King)"""
        self.hairs = color

    def get_eyes(self):
        """Get the eye color (King)"""
        return self.eyes

    def get_hairs(self):
        """Get the hair color (King)"""
        return self.hairs
