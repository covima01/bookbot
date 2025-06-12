from stats import word_count
from stats import char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:  # Use the parameter instead of hardcoding
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    count = word_count(book_text)
    chars = char_count(book_text)

    print(count)
    print(chars)


main()