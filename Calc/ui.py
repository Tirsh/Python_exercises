import input_checker


def get_data():
    numbers_type = input_checker.input_type_of_numbers("""Введите тип чисел.
    1. Рациональные
    2. Комплексные
    0. Для выхода\n""")
    if numbers_type == 0:
        return tuple('0',)
    num1 = input_checker.input_number("Введите первое число: ", numbers_type)
    num2 = input_checker.input_number("Введите второе число: ", numbers_type)
    operation = input_checker.input_operations("Введите действие: ")
    return operation, num1, num2


def out_result(data):
    if not isinstance(data, tuple):
        print(f"Результат вычислений: {data}")
    else:
        sign = '-' if data[1] < 0 else '+'
        print(f"Результат вычислений: {data[0]} {sign} {abs(data[1])}i")

