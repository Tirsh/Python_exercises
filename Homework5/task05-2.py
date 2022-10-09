def slice_from_mask(lst, mask):
    result = []
    for index, value in enumerate(mask):
        if value == "1":
            result.append(lst[index])
    return result


def is_ascending_sequences(sequences):
    if len(sequences) < 2:
        return False
    prev_item = sequences[0]
    for item in sequences[1:]:
        if prev_item >= item:
            return False
        else:
            prev_item = item
    return True


def unique_sequences(sequences):
    unique = []
    for item in sequences:
        if item not in unique:
            unique.append(item)
    return unique


def find_ascending_sequences(lst):
    list_len = len(lst)
    bin_list = [reversed(bin(item)[2:]) for item in range(1, 2 ** list_len)]
    all_sequences = [slice_from_mask(lst, item) for item in bin_list]
    ascending_sequences = list(filter(is_ascending_sequences, all_sequences))
    return unique_sequences(ascending_sequences)


print(len(find_ascending_sequences([1, 5, 2, 3, 4, 6, 1, 7])))

