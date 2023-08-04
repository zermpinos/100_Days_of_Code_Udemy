char_map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
    "'": '· − − − − ·', '!': '− · − · − −', '/': '− · · − ·', '(': '− · − − ·',
    ')': '− · − − · −', '&': '· − · · ·', ':': '− − − · · ·', ';': '− · − · − ·',
    '=': '− · · · −', '+': '· − · − ·', '-': '− · · · · −', '_': '· · − − · −',
    '"': '· − · · − ·', '$': '· · · − · · −', '@': '· − − · − ·',
}


def to_morse_code(english_plain_text):
    """
    Converts the given English plain text to Morse Code.

    Args:
        english_plain_text (str): The input English plain text.

    Returns:
        str: The corresponding Morse Code.
    """
    morse_code = ''
    for char in english_plain_text:
        if char == ' ':
            morse_code += '  '  # Add double space for word separation
        else:
            morse_code += char_map[char.upper()] + ' '  # Add a Morse Code pattern + space
    return morse_code


def main():
    english_text = input("Enter the text to convert to Morse Code: ")
    morse_code = to_morse_code(english_text)
    print("Morse Code:", morse_code)


if __name__ == '__main__':
    main()
