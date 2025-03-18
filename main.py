from stats import count_words
from stats import count_chars
from stats import sort_char_count
import sys

def get_book_text(file):
    return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_source = sys.argv[1]    

    with open(book_source) as f:
        text = get_book_text(f)
        num_words = count_words(text)
        num_chars = count_chars(text)
        sorted_count = sort_char_count(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_source}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for d in sorted_count:
            if d["character"].isalpha():
                print(f"{d['character']}: {d['count']}")
        print("============= END ===============")

main()

