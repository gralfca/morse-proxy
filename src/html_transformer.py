# Assisted by chatgpt

import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def text_to_morse(text):
    morse_text = ""
    for char in text.upper():
        if char in morse_code:
            morse_text += morse_code[char] + " "
    return morse_text.strip()

# Function to convert HTML content to Morse code text
def html_to_morse(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')

    # Find all text nodes and convert to Morse code
    for text_node in soup.find_all(text=True):
        if text_node.parent.name not in ['script', 'style']:  # Exclude script and style tags
            morse_text = text_to_morse(text_node)
            text_node.replace_with(morse_text)

    return str(soup)

def read_stdin():
    text = ""
    for line in sys.stdin:
        text += line
    return text

if __name__ == "__main__":
    input_html = read_stdin ()
    morse_html = html_to_morse(input_html)
    print(morse_html)

