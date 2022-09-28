def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")


n = input_int("Введите N: ")
num_array = list(range(-n, n+1))
print(num_array)
pos1 = input_int("Введите номер первой позиции: ")
pos2 = input_int("Введите номер второй прзиции: ")
print("Произведение элементов на позициях, равно: {}".format(
    num_array[pos1+1] * num_array[pos2+1]))
