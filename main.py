def main():
    with open("books/frankenstein.txt") as f:
        print_report(f)
def word_count(book):
    return len(book.split())

def count_letters(book):
    char_dict = {}
    for char in book:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def takeSecond(elem):
    return elem[1]

def print_report(file):
    book = file.read()
    print(f"--- Begin report of {file.name} ---")
    print(f"{word_count(book)} words found in the document\n")
    chars = count_letters(book)
    char_list = list(chars.items())
    char_list.sort(reverse=True, key=takeSecond)
    for char in char_list:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")
main()
