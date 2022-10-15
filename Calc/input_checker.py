def input_type_of_numbers(text):
    while True:
        number_string = input(text)
        if number_string.isdigit():
            num = int(number_string)
            if num in {0, 1, 2}:
                return num
        print("Некорректный ввод!")


def input_operations(text):
    while True:
        operation_string = input(text)
        if operation_string in {'+', '-', '*', '/'}:
            return operation_string
        print("Некорректный ввод!")


def input_number(text, numbers_type):
    if numbers_type == 1:
        while True:
            try:
                string_number = input(text).replace(' ', '')
                num = float(string_number)
                return num
            except ValueError:
                print("Некорректный ввод!")
    if numbers_type == 2:
        string_number = input(text).replace(' ', '')
        sign = '-' if string_number[0] == '-' else ''
        if sign == '-':
            string_number = string_number[1:]
        while True:
            first_split = string_number.split("+", 1)
            if len(first_split) == 2:
                second_split = first_split[1].split("i")
                if first_split[0].isdigit() and second_split[0].isdigit() and second_split[1] == '':
                    return int(sign + first_split[0]), int(second_split[0])
            first_split = string_number.split("-", 1)
            if len(first_split) == 2:
                second_split = first_split[1].split("i")
                if first_split[0].isdigit() and second_split[0].isdigit() and second_split[1] == '':
                    return int(sign + first_split[0]), int('-' + second_split[0])
            else:
                print("Некорректный ввод!")
