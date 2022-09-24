# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math


def input_int(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Необходимо ввести число!")


def get_pointXY(): return [input_int("Введите X: "), input_int("Введите Y: ")]  # ввод координат точки


def find_range(point_a, point_b):  # находит расстояние между точками
    return round(math.sqrt((point_b[0]-point_a[0])**2 + (point_b[1]-point_a[1])**2), 2)


print("Введите координаты первой точки:")
point_a = get_pointXY()
print("Введите координаты второй точки:")
point_b = get_pointXY()
print(find_range(point_a, point_b))
