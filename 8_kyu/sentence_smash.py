# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

def smash(words):
    """
    Concatenates a list of words into a single string, separated by spaces.

    Args:
        words (list): A list of words.

    Returns:
        str: A string containing all the words concatenated with spaces.
    """
    new_word = ""
    for word in words:
        new_word += word + " "
    return new_word.strip()