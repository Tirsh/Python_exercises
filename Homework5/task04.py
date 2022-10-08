def read_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(data)


def rle_compress(text):
    result = []
    text_list = list(text)
    symbol = text_list.pop()
    counter = 1
    while len(text_list) != 0:
        next_symbol = text_list.pop()
        if next_symbol == symbol:
            counter += 1
        else:
            result.append("{}{}".format(symbol, counter))
            counter = 1
            symbol = next_symbol
    result.append("{}{}".format(symbol, counter))
    print("Текст сжат!")
    return "".join(reversed(result))


def rle_unpacking(text):
    text_list = []
    for i in range(0, len(text), 2):
        text_list.append(text[i] * int(text[i + 1]))
    print("Текст распакован!")
    return "".join(text_list)


print("==========СЖАТИЕ ТЕКСТА===========")
text_to_compressed = read_from_file("text_to_compress.txt")
print(text_to_compressed)
compressed_text = rle_compress(text_to_compressed)
print(compressed_text)
write_to_file("compressed_text.txt", compressed_text)
print("==========РАСПАКОВКА ТЕКСТА===========")
compressed_text = read_from_file("compressed_text.txt")
print(compressed_text)
decompressed_text = rle_unpacking(compressed_text)
print(decompressed_text)
write_to_file("text_to_compress.txt", decompressed_text)
