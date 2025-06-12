from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Character class"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to set the character as dead"""
        pass

    @abstractmethod
    def is_alive(self):
        """Method to check if the character is alive"""
        pass


class Stark(Character):
    """Stark class inheriting from Character"""

    def __init__(self, first_name, is_alive=True):
        """Constructor for Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Stark method to set the character as dead"""
        self.is_alive = False

    def is_alive(self):
        """Stark method to check if the character is alive"""
        return self.is_alive
