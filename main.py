import io

def word_count(file_name):
    count = 0
    
    with open(file_name) as f:
        file_contents = f.read()
        words = file_contents.split(",")
        for word in words:
            count += len(word)

    print("This file contains", count, "words")

    
def character_count(file_name):
    char_count = {}


    with open(file_name) as f:
        file_contents = f.read()
        for char in file_contents:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


file_name = 'frankenstein.txt'
word_count(file_name)
character_count(file_name)

for char, count in character_count.items():
    print(f"The character '{char}' appears {count} times in the file.")