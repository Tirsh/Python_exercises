def list_add(list1, list2):
    list1.extend(list2)
    uniq_list = []
    for item in list1:
        if item not in uniq_list:
            uniq_list.append(item)
    return uniq_list


def find_ascending_sequences(lst):
    result = []
    if len(lst) < 2:
        return result
    for j in range(1, len(lst)):
        new_list = []
        num = lst[0]
        new_list.append(num)
        for i in range(j, len(lst)):
            if lst[i] > num:
                new_list.append(lst[i])
                num = lst[i]
        result.extend([new_list[:i] for i in range(2, len(new_list) + 1) if new_list[:i] not in result])
    return list_add(find_ascending_sequences(lst[1::]), result)


ascending_sequences = find_ascending_sequences([1, 5, 1, 2, 3, 4, 6, 1, 7])
print(ascending_sequences)
