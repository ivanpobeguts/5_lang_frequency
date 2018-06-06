import re
import sys


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(text):
    regex = r'\w+'
    words_list = re.findall(regex, text)
    frequency_dict = {word: words_list.count(word) for word in words_list}
    return sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)[:10]


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
