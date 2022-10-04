def input_int(text):
    # Функция ввода целого числа
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")


def factorial(number):
    if number == 1:
        return 1
    return factorial(number-1) * number


num = input_int("Введите число: ")
num_list = [factorial(i) for i in range(1, num+1)]
print(num_list)
