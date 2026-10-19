"""Ask the user for three favorite quotes and append them to quotes.txt.

The file is opened in append mode ('a'), so running the script again adds
new quotes without erasing the old ones.
"""

from pathlib import Path

# Output file, found relative to this script so it works from any folder
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "data" / "quotes.txt"
QUOTE_COUNT = 3


def get_quotes(count):
    """Ask the user for a number of non-empty quotes.

    Args:
        count (int): How many quotes to collect.

    Returns:
        list: The quotes entered, with surrounding spaces removed.
    """
    quotes = []
    while len(quotes) < count:
        quote = input(f"Enter favorite quote {len(quotes) + 1} of {count}: ")
        quote = quote.strip()
        if quote:
            quotes.append(quote)
        else:
            print("A quote cannot be empty. Please try again.")
    return quotes


def append_quotes(path, quotes):
    """Append quotes to a file, one quote per line.

    Args:
        path (Path or str): The file to write to. Created if missing.
        quotes (list): The quotes to write.
    """
    # 'a' appends to the end of the file and creates it if it does not exist
    with open(path, "a", encoding="utf-8") as file:
        for quote in quotes:
            file.write(quote + "\n")


def main():
    """Collect quotes from the user and save them to the file."""
    quotes = get_quotes(QUOTE_COUNT)
    try:
        append_quotes(OUTPUT_FILE, quotes)
    except PermissionError:
        print(f"Error: no permission to write to '{OUTPUT_FILE}'.")
        return
    except OSError as error:
        print(f"Error: could not write to the file ({error}).")
        return
    print(f"Saved {len(quotes)} quotes to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()