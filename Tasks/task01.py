def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")

num = input_int("Введите число: ")
for i in range(num+1):
    print((-3)**i,end=" ")