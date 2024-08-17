def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    return num_words(file_contents) , num_char(file_contents)

def num_words(file_contents):
    words = file_contents.split()
    num = 0
    for word in words:
        num += 1
    print(num)

def num_char(file_contents):
    dict_char = {}
    for char in file_contents.lower():
        if char in dict_char:
            dict_char[char] += 1
        else: 
            dict_char[char] = 1
    print(dict_char)
    return dict_char
    

main()
