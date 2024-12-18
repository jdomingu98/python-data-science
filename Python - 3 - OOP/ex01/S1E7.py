from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str):
        """Constructor for the Baratheon class."""
        super().__init__(first_name)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """
        Return the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Return the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        """
        Mark the character as not alive.
        """
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str,  is_alive: bool = True):
        """Constructor for the Lannister class."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """
        Return the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def __repr__(self):
        """
        Return the string representation of the instance.
        """
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"

    def die(self):
        """
        Mark the character as not alive.
        """
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool):
        """
        Create a Lannister character instance with custom is_alive status.
        """
        instance = cls(first_name, is_alive)
        return instance
