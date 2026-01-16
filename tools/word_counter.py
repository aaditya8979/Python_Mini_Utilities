def count_words(text):
    """
    Counts the number of words and characters in the given text.

    Parameters:
        text (str): Input text provided by the user

    Returns:
        tuple: (word_count, character_count)
    """

    # Remove leading/trailing spaces
    cleaned_text = text.strip()

    # Handle empty input
    if not cleaned_text:
        return 0, 0

    # Split text into words
    words = cleaned_text.split()

    return len(words), len(text)


if __name__ == "__main__":
    text = input("Enter text: ")

    word_count, char_count = count_words(text)

    if word_count == 0:
        print("No words entered.")
    else:
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")
