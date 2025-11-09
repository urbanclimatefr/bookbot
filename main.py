import sys
from stats import get_book_text, count_words, count_characters, sort_characters_by_frequency

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count ---------")
    count_words(get_book_text(book_path))
    print("--------- Character Count -------")
    for char, freq in sort_characters_by_frequency(count_characters(get_book_text(book_path))).items():
        if char.isalpha():  
            print(f"{char}: {freq}")
    print("============= END ===============")
