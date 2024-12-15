import sys


def print_result(message):
    """
    Analyzes a message and displays detailed statistics about its content.

    Args:
        message (str): The text to be analyzed.

    Functionality:
        - Counts the number of uppercase letters in the text.
        - Counts the number of lowercase letters in the text.
        - Counts the number of whitespace characters.
        - Counts the number of digits.
        - Calculates the number of punctuation marks.

    Displays:
        - Total number of characters in the text.
        - Number of uppercase letters.
        - Number of lowercase letters.
        - Number of punctuation marks.
        - Number of spaces.
        - Number of digits.
    """
    uppercase = sum(1 for char in message if char.isupper())
    lowercase = sum(1 for char in message if char.islower())
    spaces = sum(1 for char in message if char.isspace())
    digits = sum(1 for char in message if char.isdigit())
    punctuation_marks = len(message) - uppercase - lowercase - spaces - digits

    print(f"The text contains {len(message)} characters:")
    print(f"{uppercase} uppercase letters")
    print(f"{lowercase} lowercase letters")
    print(f"{punctuation_marks} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Main function of the program that handles input and execution.

    Functionality:
        - If no command-line argument is provided,
            it prompts the user for a message via `input`.
        - If more than one argument is provided, it raises an AssertionError.
        - If a single argument is provided,
            it is passed to the `print_result` function for processing.

    Raises:
        AssertionError: If more than one argument is provided.
    """
    if len(sys.argv) < 2:
        print("What is the text to count?")
        message = sys.stdin.readline()
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    else:
        message = sys.argv[1]
    print_result(message)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
