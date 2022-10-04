import math


def input_int(text):
    # Функция ввода целого числа
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")


def get_point_xy(): return [input_int("Введите X: "), input_int("Введите Y: ")]  # ввод координат точки


def find_range(a, b):  # находит расстояние между точками
    return round(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2), 2)


print("Введите координаты первой точки:")
point_a = get_point_xy()
print("Введите координаты второй точки:")
point_b = get_point_xy()
print(find_range(point_a, point_b))
