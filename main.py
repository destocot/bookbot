def get_contents(path):
    with open(path) as f:
        return f.read()


def get_word_count(string):
    words = string.split()
    return len(words)


def get_char_count(string):
    dict = {}
    for char in string.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


def sort_on(dict):
    return dict["count"]


def char_dict_to_list(char_count_dict):
    list = []
    for char in char_count_dict:
        list.append({"char": char, "count": char_count_dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list


def main():
    book_path = "books/frankenstein.txt"
    contents = get_contents(book_path)
    word_count = get_word_count(contents)
    char_count_dict = get_char_count(contents)
    char_count_list = char_dict_to_list(char_count_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_count_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")


main()
