import sys
from stats import count_characters, count_words, sorted_char_list, print_report


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    length = count_words(text)
    characters_dict = count_characters(text)
    char_lst = sorted_char_list(characters_dict)
    print_report(book_path, length, char_lst)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()