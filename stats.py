
def get_num_words(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    word_list = file_contents.split()
    word_count = len(word_list)
    return word_count

def get_num_characters(filepath):
    file_contents = ""
    char_dict = {}
    with open(filepath) as f:
        file_contents = f.read()
    file_contents = file_contents.lower()
    for char in file_contents:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append((char, char_dict[char]))
    sorted_list = sorted(sorted_list, key=lambda x: x[1], reverse=True)
    return sorted_list