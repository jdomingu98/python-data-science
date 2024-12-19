
def square(x: int | float) -> int | float:
    """Calculates the square of the given number."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Calculates the power of the given number by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Function that returns the inner function.
    The result of this function depends of the value of count.

    Args:
        x: int | float - base number to be used in the function
        function: function - function to be used (square or pow)
    """
    count = 0

    def inner() -> float:
        """
        Inner function that calculates the result of the function passed in
        the outer function. The result is calculated based on count value.
        variable (nonlocal) count accumulates the value of the function result.
        """
        nonlocal count
        count = function(x if count == 0 else count)
        return count
    return inner
