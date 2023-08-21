from tamil import utf8
from collections import Counter
from tamil import thirukural

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
    print(sorted(counter.items()))


def kural_char_count(kural_words):
    words = utf8.get_words(kural_words)
    print(words)
    letters = utf8.get_letters(kural_words)
    print(set(letters))
    print('Char count is : ', len(set(letters)))
    counter = Counter(letters)
    print(sorted(counter.items()))


def kural_word_count():
    kural_words = []
    verse_list = [item['verse'] for item in thirukural.thirukural]
    print(len(verse_list))
    for verse in verse_list:
        verse_words = utf8.get_words(verse)
        result_string = ' '.join(verse_words)
        kural_words.append(result_string)
    kural_words = ' '.join(kural_words)
    kural_char_count(kural_words)


if __name__ == '__main__':
    # char_count()
    kural_word_count()
