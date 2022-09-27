def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")

num = input_int("Введите n: ")
print([(1 + 1/i)**i for i in range(num)])