# Homework3 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Было:
# def sum_odd(arr):
#     return sum(arr[1::2])
# Стало:

def sum_odd(arr):
    return sum([item for index, item in enumerate(arr) if index % 2 == 1])


new_list = [2, 3, 5, 9, 3]
print(sum_odd(new_list))