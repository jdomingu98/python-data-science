from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class representing a character.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Constructor for the Character class.

        Args:
            first_name (str): first name of the character
            is_alive (bool, optional): character is alive. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        Abstract method to change the health state of the character.
        Must be implemented by subclasses.
        """
        pass


class Stark(Character):
    """
    Represents a member of the Stark family, inheriting from Character.
    """

    def die(self):
        """Method to change the health state of the character."""
        self.is_alive = False
