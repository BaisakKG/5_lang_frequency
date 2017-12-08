from collections import Counter

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return file_handler.read()


def get_most_frequent_words(file_text, most_common_words_count):
    cleaned_list = []
    for word in file_text.split():
        cleaned_list.append(word.strip('.,!-:"\()\'').lower())
        
    print(Counter(cleaned_list).most_common(int(float(most_common_words_count))))

if __name__ == '__main__':
    file_text = load_data(r'd:\PythonScript\Devman\RomeoAndJuliet.txt')
    get_most_frequent_words(file_text, 10)

