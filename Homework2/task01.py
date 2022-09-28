from curses.ascii import isdigit


def input_float(text):
    # Функция ввода вещественного числа
    while (True):
        try:
            number = float(input(text))
            return number
        except ValueError:
            print('Необходимо ввести число! (разделитель ".")')


number = input_float("Введите вещественное число: ")
number_as_string = str(number)
int_list = list((map(int, filter(isdigit, number_as_string))))
numbers_sum = sum(int_list)
print("Сумма цифр: {}".format(numbers_sum))
