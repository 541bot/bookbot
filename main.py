from stats import count_words
from stats import count_chars
from stats import sort_char_count

def get_book_text(file):
    return file.read()

def main():
    book_source = "books/frankenstein.txt"
    with open(book_source) as f:
        text = get_book_text(f)
        num_words = count_words(text)
        num_chars = count_chars(text)
        sorted_count = sort_char_count(num_chars)
        # print(f"{num_words} words found in the document")
        # print(num_chars)
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

