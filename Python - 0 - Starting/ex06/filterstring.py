import sys
from ft_filter import ft_filter


def main():
    """
    Main function to process command-line arguments
    and filter a message based on word length.

    This function:
        - Ensures that exactly two command-line arguments are provided.
        - The first argument is treated as a message (string).
        - The second argument is treated as a number (integer)
            which sets a threshold for word length.
        - The function splits the message into words
            and filters out those with a length greater
            than the provided threshold.
        - Prints the filtered list of words.

    Raises:
        AssertionError: If the number of arguments is not exactly two,
            or if the second argument cannot be converted to an integer.

    Args:
        None (Arguments passed through the command line).

    Returns:
        None: The result is printed directly to the console.
    """
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        text = sys.argv[1]
        number = int(sys.argv[2])
        filtered_msg = ft_filter(lambda word: len(word) > number, text.split())
        print(filtered_msg)
    except ValueError:
        raise AssertionError("the arguments are bad")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
