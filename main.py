# main.py

import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """
    Reads the contents of the file at the given filepath and returns it as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found. Please check the filepath."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)

    if "File not found" in book_text or "An error occurred" in book_text:
        print(book_text)
    else:
        num_words = get_num_words(book_text)
        char_counts = get_char_counts(book_text)
        sorted_chars = sort_char_counts(char_counts)

        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

# Call main to execute the program
if __name__ == "__main__":
    main()
