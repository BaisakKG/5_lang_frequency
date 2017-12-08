import operator

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(file_text):
    words = dict()
    for word in file_text.split():
        cleaned_word = word.strip('.,!-:"\()\'').lower()
        if cleaned_word not in words:
            words[cleaned_word] = 0
        words[cleaned_word] += 1
    
    word_items = words.items()
    word_count_items = sorted(word_items, key=operator.itemgetter(1), reverse=True)
    print(word_count_items[:10])


if __name__ == '__main__':
    file_text = load_data(r'd:\PythonScript\Devman\RomeoAndJuliet.txt')
    get_most_frequent_words(file_text)

