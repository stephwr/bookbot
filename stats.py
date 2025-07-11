# stats.py

def get_num_words(text):
    """
    Counts and returns the number of words in the given text string.
    """
    words = text.split()
    return len(words)

def get_char_counts(text):
    """
    Returns a dictionary mapping each character (in lowercase) to the number of times it appears.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary has the structure {"char": <character>, "num": <count>}.
    Only includes alphabetical characters. Sorted from most to least frequent.
    """
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars
