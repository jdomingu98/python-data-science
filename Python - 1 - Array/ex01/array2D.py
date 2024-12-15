import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function takes a 2D array, prints its shape, and returns a truncated
    version of the array using slicing. Handles errors for invalid input.

    Parameters:
    - family: A 2D array (list of lists).
    - start: The starting index for slicing.
    - end: The ending index for slicing.

    Returns:
    The truncated version of the array.
    """
    arr = np.array(family)

    assert arr.ndim == 2, "Input must be a 2D list."

    print(f"My shape is : {arr.shape}")

    sliced = arr[start:end]
    print(f"My new shape is : {sliced.shape}")

    return sliced.tolist()
