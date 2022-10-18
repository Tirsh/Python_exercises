import input_checker, loger


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
    loger.write_log(f"Ввод данных: тип({numbers_type}), число1({num1}), число2({num2}), действие({operation})")
    return operation, num1, num2


def out_result(data):
    loger.write_log(f"Вывод результата на экран: {data}")
    if not isinstance(data, tuple):
        print(f"Результат вычислений: {data}")
    else:
        sign = '-' if data[1] < 0 else '+'
        if data[0] == 0 and data[1] != 0:
            print(f"Результат вычислений: {data[1]}i")
        elif data[1] == 0 and data[0] != 0:
            print(f"Результат вычислений: {data[0]}")
        elif data[0] == 0 and data[1] == 0:
            print(f"Результат вычислений: 0")
        else:
            print(f"Результат вычислений: {data[0]} {sign} {abs(data[1])}i")

