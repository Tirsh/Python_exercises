from random import randrange, choice


def list_mixer(array):
    length = len(array)
    mixed_list = []
    pos_list = list(range(length))
    n = length
    while n > 0:
        index = randrange(0, n)
        mixed_list.append(array[pos_list[index]])
        pos_list.pop(index)
        n -= 1
    return mixed_list


def list_mixer2(array):  # вариант с random.choice()
    length = len(array)
    mixed_list = []
    pos_list = list(range(length))
    while True:
        place = choice(pos_list)
        pos_list.remove(place)
        mixed_list.append(array[place])
        if len(mixed_list) == length:
            break
    return mixed_list


print(list_mixer(range(-10, 10, 1)))
