import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculates the Body Mass Index (BMI) for a list of heights and weights.

    Parameters:
        - height: A list of heights in meters.
        - weight: A list of weights in kilograms.

    Returns:
        A list of BMI values for each pair using the formula:
            BMI = weight / (height ** 2)

    Raises:
        - AssertionError:
            - If the lengths of `height` and `weight` lists are not equal.
            - If any element in `height` or `weight` is not int or float.
    """
    w = np.array(weight)
    h = np.array(height)

    assert w.size == h.size, "Lists are not of equal length."
    assert (
        np.issubdtype(w.dtype, np.integer)
        or np.issubdtype(w.dtype, np.floating)
    ), "The list has values that are neither integers nor floats."

    assert (
        np.issubdtype(h.dtype, np.integer)
        or np.issubdtype(h.dtype, np.floating)
    ), "The list has values that are neither integers nor floats."

    return np.array(w / (h ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values
    and return a list of booleans indicating whether each BMI
    is greater than the specified limit.

    Args:
        bmi: A list of BMI values, each of which can be
            an integer or a float.
        limit: The BMI threshold. Each element is compared to this limit.

    Returns:
        A list of booleans, where each element is `True` if the corresponding
            BMI value is greater than the limit, and `False` otherwise.

    Raises:
        AssertionError: If any element is neither an integer nor a float.
    """
    arr = np.array(bmi)
    assert (
        np.issubdtype(arr.dtype, np.integer)
        or np.issubdtype(arr.dtype, np.floating)
    ), "The list have values that not are integer or float."
    return (arr > limit).tolist()
