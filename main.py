import sys
from stats import word_count
from stats import char_count
from stats import sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:  # Use the parameter instead of hardcoding
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)


    count = word_count(book_text)
    chars = char_count(book_text)


    #print(count)
    #print(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    sorted_dict = sorted_list(chars)
    for item in sorted_dict:
        print(item)
    print("============= END ===============")


main()