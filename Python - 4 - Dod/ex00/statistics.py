from typing import Any


def ft_mean(numbers: list) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def ft_median(numbers: list) -> float:
    """Calculate the meadian of a list of numbers."""
    n = len(numbers)
    numbers.sort()
    if n % 2 == 0:
        result = numbers[n // 2 - 1] + numbers[n // 2]
    else:
        result = numbers[n // 2]

    return result


def ft_quartile(numbers: list) -> list:
    """Calculate q1 and q3 of a list of numbers and returns it as an array."""
    n = len(numbers)
    numbers.sort()
    return [float(numbers[n // 4]), float(numbers[n * 3 // 4])]


def ft_var(numbers: list) -> float:
    """Calculate the variance of a list of numbers."""
    n = len(numbers)
    mean = ft_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / n


def ft_std(numbers: list) -> float:
    """Calculate the standard deviation of a list of numbers."""
    std = ft_var(numbers) ** 0.5
    return std


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate the statistics of a list of numbers.

    Valid statistics are: mean, median, quartile, std, var
    Other names will be ignored.

    If no valid statistics are provided, the function will return None.

    If the list of numbers contains invalid values,
    the function will print "ERROR".
    """
    numbers = list(args)
    valid_operations = list(filter(
                        lambda x: x in ['mean', 'median',
                                        'quartile', 'std', 'var'],
                        kwargs.values()
                    ))

    if not valid_operations:
        return

    valid_numbers = [x for x in numbers
                     if isinstance(x, (int, float)) and x >= 0]

    if len(numbers) != len(valid_numbers):
        print("ERROR")

    for x in valid_operations:
        func = globals().get(f"ft_{x}")
        if func and len(valid_numbers) > 0:
            print(f"{x} : {func(valid_numbers)}")
        else:
            print("ERROR")
