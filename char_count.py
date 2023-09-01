from tamil import utf8
from kural import thirukural
from collections import Counter
import re

INPUT = ('தமிழ் ஔவை ஈழ பழுவூர் ஸ்ரீமயூரபுருஷன் வீட்டில் லீவு நாளான மூன்றாம் தேதி ஞாயிறு ஏழு மணி விருந்துக்கு '
         'டிஃபன் ஸ்பெஷல் பக்ஷணங்களாக சூடான இட்லி பூரி ஊத்தப்பம் ஆமவடை கூட்டு ஹல்வா நுங்குஜூஸ் ஐஸ்டீ சாப்பிட்டாள் '
         'ஈவது விலக்கேல் ஏற்பது இகழ்ச்சி ஐயமிட்டு உண் ஊக்கமது கைவிடேல் மூதுரை ஒளவை கூறிய ஆத்திசூடி நூலின் '
         'தீஞ்சுவை மொழி அஃதே எங்கள் பூவுலக நெறி தமிழ் குடி ஐயன் ஆதி முருகன் சூர உலகிற்கு ஈந்தளித்த நீர் திருமந்திரம் '
         'ஓம் நமசிவாயெனும் பஞ்சாட்சரம் அஃதே மூப்பு பிணி ஏழுபிறப்பு ஊழி இம்மை மறுமை ஒழிக்குங்கூறு')


def char_count():
    words = utf8.get_words(INPUT)
    print(words)
    letters = utf8.get_letters(INPUT)
    print(set(letters))
    print('Char count is : ', len(set(letters)))
    counter = Counter(letters)
    print(sorted(counter))


def get_tamil_letter():
    tamil_letters = (
            utf8.uyir_letters + utf8.mei_letters + utf8.uyirmei_letters
            # + utf8.grantha_mei_letters + utf8.grantha_agaram_letters
            # + utf8.grantha_uyirmei_letters
    )
    tamil_letters.append(utf8.aytham_letter)
    return tamil_letters


def kural_char_count(words):
    letters = set(utf8.get_letters(words))
    filtered_letters = remove_chars(letters)
    kural_letters = sorted(filtered_letters)
    tamil_letters = get_tamil_letter()
    missing_items = [item for item in tamil_letters if item not in kural_letters]
    print('Letters Used in Kural : ', kural_letters)
    print('Missing letters in Kural : ', missing_items)
    print('Missing letters count : ', len(tamil_letters) - len(filtered_letters))
    print('Length of Missing letters in Kural : ', len(missing_items))


# Function to remove dot, space, and numbers from a string
def remove_chars(chars):
    filtered = [re.sub(r'[ .0-9]', '', word) for word in chars]
    return [char for char in filtered if char != '']


def write_to_file(u_words):
    with open("words/kural_words.txt", 'w') as f:
        for u_word in u_words:
            f.writelines(u_word + '\n')
    f.close()


def kural_word_count():
    kural_words = []
    verse_list = [item['kural'] for item in thirukural.thirukural]
    print(len(verse_list))
    for verse in verse_list:
        verse_words = utf8.get_words(verse)
        print(verse_words)
        result_string = ' '.join(verse_words)
        kural_words.append(result_string)
    kural_words = ' '.join(kural_words)
    words = set(utf8.get_words(kural_words))
    write_to_file(list(words))
    # print('Unique words : ', len(words))
    # kural_char_count(words)


if __name__ == '__main__':
    # char_count()
    kural_word_count()
