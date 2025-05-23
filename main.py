from stats import count_characters, count_words, sorted_char_list, print_report


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    length = count_words(text)
    characters_dict = count_characters(text)
    char_lst = sorted_char_list(characters_dict)
    print_report(book_path, length, char_lst)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()