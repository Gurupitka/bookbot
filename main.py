from stats import get_word_count,get_symbol_counts,get_sorted_symbol_count
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    num_words = get_word_count(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counts = get_symbol_counts(book_text)
    sortedCounts = get_sorted_symbol_count(counts)
    for symb in sortedCounts:
        if symb.isalpha():
            print(f"{symb}: {sortedCounts[symb]}")
    print("============= END ===============")

main()