from random import randrange


def list_mixer(array):
    length = len(array)
    mixed_list = []
    while (True):
        place = randrange(0, length)
        if (place not in mixed_list):
            mixed_list.append(place)
        if len(mixed_list) == length:
            break
    for i in range(length):
        mixed_list[i] = array[mixed_list[i]]
    return mixed_list


print(list_mixer([2, 2, 5, 5, 5, 10, 10, 7, 7, 7]))
