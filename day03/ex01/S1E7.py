from S1E9 import Character

class Baratheon(Character):
    """Baratheon class inheriting from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon class"""
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return 

    def die(self):
        """Baratheon method to set the character as dead"""
        self.is_alive = False

    def is_alive(self):
        """Baratheon method to check if the character is alive"""
        return self.is_alive



class Lannister(Character):
    """Lannister class inheriting from Character"""

    def __init__(self):
        self.family_name = "Lanister"

    def die(self):
        """Stark method to set the character as dead"""
        self.is_alive = False

    def is_alive(self):
        """Stark method to check if the character is alive"""
        return self.is_alive

    # decorateur
    def create_lannister():
        pass
