def find_fractional_diff(array):
    fractional_map = map(lambda num: num % 1, array)
    fractional_list = list(filter(lambda x: x != 0, fractional_map))
    fractional_min = min(fractional_list)
    fractional_max = max(fractional_list)
    return round(fractional_max - fractional_min, 2)


new_list = [1.1, 1.2, 3.1, 5, 10.01]
print(find_fractional_diff(new_list))
