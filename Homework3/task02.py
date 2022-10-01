def pairs_multiplication(array):
    length = len(array)
    iterations = length // 2 + length % 2
    return [array[i] * array[-i - 1] for i in range(iterations)]


new_list = [2, 3, 4, 5, 6]
print(pairs_multiplication(new_list))
