from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Baratheon class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """String representation of the Baratheon character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Representation of the Baratheon character"""
        return self.__str__()

    def die(self):
        """Baratheon method to set the character as dead"""
        self.is_alive = False

    def is_alive(self):
        """Baratheon method to check if the character is alive"""
        return self.is_alive


class Lannister(Character):
    """Lannister class inheriting from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Lannister class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """String representation of the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Representation of the Lannister character"""
        return self.__str__()

    def die(self):
        """Stark method to set the character as dead"""
        self.is_alive = False

    def is_alive(self):
        """Stark method to check if the character is alive"""
        return self.is_alive

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Factory method to create a Lannister character"""
        return cls(first_name, is_alive)
