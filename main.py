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
    

def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    character_count = {}
    for c in text.lower():
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count


def sort_on(dict):
    return dict["num"]


def sorted_char_list(dict):
    char_list = []
    for k in dict:
        if k.isalpha():
            char_list.append({"char": k, "num": dict[k]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_report(path, int, lst):
    print(f"--- Report of {path} ---")
    print(f"The book is {int} words long. \n")
    for dict in lst:
        print(f"The {dict['char']} character was found {dict['num']} times")
    print("--- End report ---")


main()