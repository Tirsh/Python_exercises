def input_float(text):
    # Функция ввода вещественного числа в границах 10^{-1} ≤ d ≤10^{-10}
    while True:
        try:
            text_in = input(text)
            num = float(text_in)
            if 1e-1 >= num >= 1e-10:
                return num
            else:
                raise ValueError
        except ValueError:
            print("Необходимо ввести вещественное число в рамках 10^{-1} ≤ d ≤10^{-10}!")


def count_pi(accuracy):
    x1, x2 = 0, 0
    for i in range(1, 50000000000, 4):
        x1 = x2 + 4 / i
        x2 = x1 - 4 / (i+2)
        if x1-x2 <= accuracy:
            return x2


d = input_float("Задайте точность d: ")
print(count_pi(d))
