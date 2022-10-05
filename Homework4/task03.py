def input_subseq():
    while True:
        try:
            num_str = input('Введите последовательность чисел через " ": ')
            return list(map(int, num_str.split()))
        except ValueError:
            print("Некорректный ввод")


def filter_only_one(lst):
    return [num for num in lst if lst.count(num) == 1]


list1 = input_subseq()
print(filter_only_one(list1))
