# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            if number < 1 or number > 4:
                raise ValueError
            return number
        except ValueError:
            print("Необходимо ввести число, от 1 до 4!")


plane = {   # словарь возможный варианов расположения точки
    1: "0 < X < ∞; 0 < Y < ∞",
    2: "-∞ < X < 0; 0 < Y < ∞",
    3: "-∞ < X < 0; -∞ < Y < 0",
    4: "0 < X < ∞; -∞ < Y < 0"
}

print(plane[input_int("Задайте номер четверти: ")])
