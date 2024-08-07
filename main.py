def main():
    # opens frankenstien.txt file
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_word_count(file_contents)
    num_chars = get_count_per_char(file_contents)

    print(f"{num_words} words found in the document\n")
     
    for key in num_chars:
        print_letter_and_amounts(key,num_chars[key])
    
    print("--- End report ---")


def get_word_count(input_string):
    words = input_string.split()
    return len(words)

def get_count_per_char(text):
    text = text.lower()
    new_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_dict = {}
   
    for char in text:
        if char in new_list:
            if char in new_dict:
                new_dict[char] += 1
            else:
                new_dict[char] = 1
    
    sorted_value_descend_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_value_descend_dict

def print_letter_and_amounts(char, num):
    print(f"The '{char}' character was found {num} times")
    
def get_book_text(text):
    with open(text) as f:
        return f.read()


main()

