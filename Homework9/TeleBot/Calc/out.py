import loger


def out_result(data):
    loger.write_log(f"Вывод результата на экран: {data}")
    if not isinstance(data, tuple):
        return f"Результат вычислений: {data}"
    else:
        sign = '-' if data[1] < 0 else '+'
        if data[0] == 0 and data[1] != 0:
            return f"Результат вычислений: {data[1]}i"
        elif data[1] == 0 and data[0] != 0:
            return f"Результат вычислений: {data[0]}"
        elif data[0] == 0 and data[1] == 0:
            return f"Результат вычислений: 0"
        else:
            return f"Результат вычислений: {data[0]} {sign} {abs(data[1])}i"
