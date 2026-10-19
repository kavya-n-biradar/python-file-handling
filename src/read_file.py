"""Read a text file and report its word, line and character counts.

Usage:
    python src/read_file.py                 (reads data/input.txt)
    python src/read_file.py path/to/file    (reads a different file)
"""

import sys
from pathlib import Path

# Default input file, found relative to this script so it works from any folder
DEFAULT_FILE = Path(__file__).resolve().parent.parent / "data" / "input.txt"


def analyze_text(text):
    """Count the words, lines and characters in a piece of text.

    Args:
        text (str): The text to analyze.

    Returns:
        tuple: (word_count, line_count, character_count)
    """
    words = len(text.split())
    lines = len(text.splitlines())
    characters = len(text)
    return words, lines, characters


def read_file(path):
    """Read a text file and return its contents.

    Args:
        path (Path or str): The file to read.

    Returns:
        str: The contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    # 'r' opens the file for reading only; 'with' closes it automatically
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def main():
    """Read the file, print its statistics and handle errors."""
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE

    try:
        text = read_file(path)
    except FileNotFoundError:
        print(f"Error: the file '{path}' was not found.")
        print("Check the file name and location, then try again.")
        return
    except PermissionError:
        print(f"Error: you do not have permission to read '{path}'.")
        return
    except UnicodeDecodeError:
        print(f"Error: '{path}' is not a readable UTF-8 text file.")
        return

    if not text.strip():
        print(f"The file '{path}' is empty.")
        return

    words, lines, characters = analyze_text(text)
    print(f"File: {path}")
    print(f"Total words: {words}")
    print(f"Total lines: {lines}")
    print(f"Total characters: {characters}")


if __name__ == "__main__":
    main()