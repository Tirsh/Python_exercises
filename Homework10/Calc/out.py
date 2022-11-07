import loger


def complex_format(data):
    if data[1] >= 0:
        text = f"({data[0]} + {data[1]}i)"
    else:
        text = f"({data[0]} - {abs(data[1])}i)"
    return text


def out_result(data, result):
    loger.write_log(f"Вывод результата на экран: {result}")
    if not isinstance(result, tuple):
        return f"Результат вычислений: {data[1]} {data[0]} {data[2]} = {round(result, 2)}"
    else:
        sign = '-' if result[1] < 0 else '+'
        if result[0] == 0 and result[1] != 0:
            return f"Результат вычислений1: " \
                   f"{complex_format(data[1])} {data[0]} {complex_format(data[2])} = {round(result[1], 2)}i "
        elif result[1] == 0 and result[0] != 0:
            return f"Результат вычислений2: " \
                   f"{complex_format(data[1])} {data[0]} {complex_format(data[2])} = {round(result[0])}"
        elif result[0] == 0 and result[1] == 0:
            return f"Результат вычислений: 0"
        else:
            return f"Результат вычислений3: " \
                   f"{complex_format(data[1])} {data[0]} {complex_format(data[2])} = " \
                   f"{round(result[0])} {sign} {round(abs(result[1]), 2)}i"
