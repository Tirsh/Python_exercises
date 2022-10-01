from curses.ascii import isdigit


def input_int(text):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            return int(text_in)
        else:
            print("Необходимо ввести число!")


def fibo(num):
    if num <= 1:
        return num
    if num > 1:
        return fibo(num - 1) + fibo(num - 2)


def nega_fibo(num):
    if num >= -1:
        return -num
    if num < -1:
        return nega_fibo(num + 2) - nega_fibo(num + 1)


def fibo_list(num):
    num_list = []
    for i in range(-num, num + 1):
        if i < 0:
            num_list.append(nega_fibo(i))
        if i >= 0:
            num_list.append(fibo(i))
    return num_list


number = input_int("Введите число: ")
print(fibo_list(number))
