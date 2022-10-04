input_string = input("Введите день недели: ")
if input_string.isdigit():
    day_of_the_week = int(input_string)
    if 0 < day_of_the_week <= 7:
        print(f'{day_of_the_week} -> Yes' if 6 <= day_of_the_week <= 7 else f'{day_of_the_week} -> No')
    else:
        print("Число должно быть в диапазоне от 1 до 7!")
else:
    print("День недели должен быть числом")
