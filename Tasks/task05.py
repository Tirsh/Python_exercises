def input_int(text):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            return int(text_in)
        else:
            print("Необходимо ввести число!")


a = input_int("A: ")
b = input_int("B: ")
c = input_int("C: ")