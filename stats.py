def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
       return (file.read()) 

# function that accetpt text from the book as a string and returns the number of words in the text
def count_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    return num_words

# function that accepts text from the book as a string and returns the number of times each character appears in the text
def count_characters(text):
    char_count = {}
    for char in text:
        char = char.lower()  # Normalize to lowercase
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_characters_by_frequency(char_count):
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))