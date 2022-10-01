from curses.ascii import isdigit


def input_int(text):
    # Функция ввода целого числа
    while (True):
        text_in = input(text)
        if text_in.isdigit():
            return int(text_in)
        else:
            print("Необходимо ввести число!")


def dec_to_bin(number):
    if number < 2:
        return str(number)
    else:
        return "{}{}".format(dec_to_bin(number // 2), number % 2)


num = input_int("Введите число: ")
print(dec_to_bin(num))
