def sum_odd(arr):
    return sum(arr[1::2])


# def sum_odd(arr):
#     return sum([item for index, item in enumerate(arr) if index % 2 == 1])


new_list = [2, 3, 5, 9, 3]
print(sum_odd(new_list))
