from curses.ascii import isdigit


# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
input_string = input("Введите день недели: ")
if input_string.isdigit():
    day_of_the_week = int(input_string)
    if day_of_the_week > 0 and day_of_the_week <= 7:
        print(f'{day_of_the_week} -> Yes' if day_of_the_week >=
              6 and day_of_the_week <= 7 else f'{day_of_the_week} -> No')
    else:
        print("Число должно быть в диапозоне от 1 до 7!")
else:
    print("День недели должен быть числом")
