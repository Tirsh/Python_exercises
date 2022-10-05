def input_int(text):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            return int(text_in)
        else:
            print("Необходимо ввести число!")


def prime_factors(number):
    for i in range(2, number):
        if number % i == 0:
            return [*prime_factors(number//i), i]
    return [number]


num = input_int("Введите число: ")
print(prime_factors(num))
