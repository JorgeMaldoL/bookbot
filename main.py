def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"---Begin report of books/frankenstein.txt ---\n")
    print(f"{num_words(file_contents)} found in the document\n")
    char_counts = num_char(file_contents)
    sorted_chars = sort_char(char_counts)
    sorted_chars.sort(reverse=True, key=sort_on)
    for char_info in sorted_chars:
        char = char_info["char"]
        num = char_info["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")
    print(f"--- End report ---")

def num_words(file_contents):
    words = file_contents.split()
    num = len(words)
    return num

def num_char(file_contents):
    dict_char = {}
    for char in file_contents.lower():
        if char in dict_char:
            dict_char[char] += 1
        else: 
            dict_char[char] = 1
    return dict_char

def sort_char(dict_char):
    list_char = []
    new_dict = {}
    for char in dict_char:
        if char.isalpha():
            new_dict = {"char": char, "num": dict_char[char]}
            list_char.append(new_dict)
    return list_char

def sort_on(new_dict):
    return new_dict["num"]  

main()
