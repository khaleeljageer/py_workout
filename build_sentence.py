from tamil import utf8
import random
import re

tamil_characters = set(utf8.uyir_letters + [utf8.aytham_letter] + utf8.mei_letters + utf8.uyirmei_letters)


# Function to remove dot, space, and numbers from a string
def remove_chars(word_list):
    filtered = [re.sub(r'[ .0-9]', '', s_word) for s_word in word_list]
    return [char for char in filtered if char != '']


def get_tamil_words():
    with open("words/tamil_words.txt", 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        f.close()
    return sorted(lines, key=lambda x: random.random())


# word_corpus = kural_word_count()
word_corpus = get_tamil_words()

# Create a list of available words for each character
word_dict = {char: [] for char in tamil_characters}
for c_word in word_corpus:
    used_chars = set(utf8.get_letters(c_word.replace(' ', '')))
    for char in used_chars:
        word_dict[char].append(c_word)


def build_sentence():
    # Find a combination
    resulting_word_list = find_combination(list(tamil_characters), [])
    # Print the result
    print(resulting_word_list)
    return resulting_word_list


# Backtracking function to find a combination
def find_combination(remaining_chars, current_words):
    print('finding combination')
    if not remaining_chars:
        return current_words

    char = remaining_chars[0]
    print('finding combination : ', char)
    if char in word_dict and word_dict[char]:
        print('Char: ', char)
        for word in word_dict[char]:
            print('Word: ', word)
            new_words = current_words + [word]
            new_remaining_chars = remaining_chars.copy()
            new_remaining_chars.remove(char)
            new_word_dict = {key: value.copy() for key, value in word_dict.items()}
            new_word_dict[char].remove(word)
            result = find_combination(new_remaining_chars, new_words)
            print('Result: ', result)
            if result:
                return result
    return None


def test_result(_result):
    print("Length of Tamil Characters: ", len(tamil_characters))
    all_words = ''.join(_result)
    used_characters = set(utf8.get_letters(all_words))
    print("Used Tamil Characters: ", sorted(used_characters))
    print("Length of Used Tamil Characters: ", len(used_characters))
    # Check if all tamil_characters have been used
    all_characters_used = all(char in used_characters for char in tamil_characters)

    if all_characters_used:
        print("All Tamil characters have been used.")
    else:
        missing_characters = [char for char in tamil_characters if char not in used_characters]
        print("Missing Tamil characters:", sorted(missing_characters))
        print("Length of Missing Tamil characters:", len(missing_characters))


if __name__ == '__main__':
    s_result = build_sentence()
    if s_result is None:
        print('No match found')
    else:
        test_result(s_result)
