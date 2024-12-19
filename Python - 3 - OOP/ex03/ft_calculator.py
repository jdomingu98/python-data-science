
class calculator:
    """
    Represents a calculator that can
    add, multiply, subtract, and divide an array of numbers.
    """
    def __init__(self, object) -> None:
        """Constructor for the calculator class."""
        self.array = object

    def __add__(self, object) -> None:
        """Add a number to every element of the array."""
        self.array = list(map(lambda x: x + object, self.array))
        print(self.array)

    def __mul__(self, object) -> None:
        """Multiply a number to every element of the array."""
        self.array = list(map(lambda x: x * object, self.array))
        print(self.array)

    def __sub__(self, object) -> None:
        """Sustract a number to every element of the array."""
        self.array = list(map(lambda x: x - object, self.array))
        print(self.array)

    def __truediv__(self, object) -> None:
        """Divide a number to every element of the array."""
        try:
            self.array = list(map(lambda x: x / object, self.array))
            print(self.array)
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)
