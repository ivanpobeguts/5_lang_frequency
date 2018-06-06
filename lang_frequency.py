import re
import sys
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text):
    WORDS_AMOUNT = 10
    words_list = re.findall(r'\w+', text)
    return Counter(words_list).most_common(WORDS_AMOUNT)


if __name__ == '__main__':
    try:
        text = load_data(sys.argv[1])
        frequent_words = get_most_frequent_words(text)
        for word, amount in frequent_words:
            print('The word "{}" occurs in the text "{}" times'.format(word, amount))
    except IndexError:
        print('Specify file path.')
    except FileNotFoundError:
        print('File not found.')
