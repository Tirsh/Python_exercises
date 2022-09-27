def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")

num = input_int("Введите число: ")
print([3*i+1 for i in range(1, n+1)])