import random

DEGREES = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}


def input_int(text):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            return int(text_in)
        else:
            print("Необходимо ввести число!")


def create_multipliers(grade):
    return [random.randrange(0, 100) for _ in range(grade + 1)]


def int_to_degree(num):
    if num <= 1:
        return ""
    if num < 10:
        return DEGREES[num]
    return f"{DEGREES[num // 10]}{DEGREES[num % 10]}"


def create_polinom(degree):
    multipliers = create_multipliers(degree)
    result_list = []
    for element, item in enumerate(multipliers):
        if item != 0 and element > 0:
            result_list.append(f'{item}x{int_to_degree(element)}')
        elif item != 0 and element == 0:
            result_list.append(f'{item}')
    return str.join(' + ', reversed(result_list)) + ' = 0'


k = input_int("Введите натуральную степень k: ")
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(create_polinom(k))
