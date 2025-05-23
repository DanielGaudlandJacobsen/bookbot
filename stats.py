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
    print(f"{int} words found in the document.\n")
    for dict in lst:
        print(f"{dict['char']}: {dict['num']}")
    print("--- End report ---")