import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
from stats import get_num_words

from stats import get_num_characters

from stats import sorted_list  


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    word_count = get_num_words(sys.argv[1])
    character_count = get_num_characters(sys.argv[1])
    character_count_filtered = {}
    for char in character_count:
        if char.isalpha():
            character_count_filtered[char] = character_count[char]
    character_count_sorted = sorted_list(character_count_filtered)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in character_count_sorted:
        just_char, num = char
        print(f"{just_char}: {num}")
    print("============= END ===============")

main()