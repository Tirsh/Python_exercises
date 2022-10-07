def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def delete_word_in_text(text, removed_phrase):
    string_list = text.split()
    return " ".join(list(filter(lambda x: True if x.find(removed_phrase) == -1 else False, string_list)))


phrase = "abc"
print(delete_word_in_text(read_from_file("text.txt"), phrase))
