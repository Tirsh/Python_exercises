# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт
# номер четверти плоскости, в которой находится эта точка
def input_int_not_null(text):
    # Функция ввода целого числа
    while (True):
        try:
            number = int(input(text))
            if number == 0:
                raise ValueError
            return number
        except ValueError:
            print("Необходимо ввести число, не равное нулю!")


print("Введите координаты X ≠ 0 и Y ≠ 0")
x = input_int_not_null("Введите X: ")
y = input_int_not_null("Введите Y: ")
if (x > 0 and y > 0):
    print(f"X={x}, Y={y} -> 1")
elif (x < 0 and y > 0):
    print(f"X={x}, Y={y} -> 2")
elif (x < 0 and y < 0):
    print(f"X={x}, Y={y} -> 3")
else:
    print(f"X={x}, Y={y} -> 4")
