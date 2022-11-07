import loger


def make_sum(a, b):
    if not isinstance(a, tuple):
        return a + b
    else:
        return a[0] + b[0], a[1] + b[1]


def make_sub(a, b):
    if not isinstance(a, tuple):
        return a - b
    else:
        return a[0] - b[0], a[1] - b[1]


def make_mult(a, b):
    if not isinstance(a, tuple):
        return a * b
    else:
        return a[0] * b[0], a[1] * b[1]


def make_div(a, b):
    if not isinstance(a, tuple):
        return a / b
    else:
        return a[0] / b[0], a[1] / b[1]


operations = {'+': make_sum, '-': make_sub, '*': make_mult, '/': make_div}


def make_calc(data):
    result = operations[data[0]](data[1], data[2])
    loger.write_log(f"Произведена калькуляция: ({data[1]} {data[0]} {data[2]}), результат({result})")
    return data, result
