import sys


def morse_code(list_char):
    """
    Converts a list of characters into their Morse code representations.

    This function takes a list of characters and converts each character into
    its corresponding Morse code, as defined in the NESTED_MORSE dictionary.

    Args:
        list_char: A list of characters to be converted into Morse code.

    Returns:
        A string representing the Morse code for the input characters,
        with each Morse code letter separated by a space.
    """
    NESTED_MORSE = {
        ' ': '/',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    }
    morse_code = []
    for char in list_char:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_code.append(NESTED_MORSE[char.upper()])
    return " ".join(morse_code)


def main():
    """
    Main function that processes command-line arguments, validates input,
    and prints the Morse code representation of the input text.

    Functionality:
        - Checks if exactly one command-line argument is provided.
        - Validates that the argument is a string.
        - Converts the string to Morse code and prints the result.

    Raises:
        AssertionError:
            - If the number of command-line arguments is not equal to 2.
            - If the argument is not a string.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")
    text = sys.argv[1]
    if not isinstance(text, str):
        raise AssertionError("the arguments are bad")
    print(morse_code(list(text)))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")
