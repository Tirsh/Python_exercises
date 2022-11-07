def input_type_of_numbers(number, numbers):
    return number in numbers


def input_operations(operation):
    if operation in {'+', '-', '*', '/'}:
        return True
    else:
        return False


def numbers_split_and_compere(spliter, num_str, sign):
    first_split = num_str.split(spliter, 1)
    if len(first_split) == 2:
        second_split = first_split[1].split("i")
        if first_split[0].isdigit() and \
                (second_split[0].isdigit() or not second_split[0]) and second_split[1] == '':
            if first_split[0].isdigit() and second_split[0].isdigit():
                return int(sign + first_split[0]), int(spliter + second_split[0])
            if first_split[0].isdigit() and not second_split[0]:
                return int(sign + first_split[0]), int(spliter+"1")
    elif len(first_split) == 1:
        if first_split[0].isdigit():
            return int(sign + first_split[0]), 0
        second_split = first_split[0].split("i")
        if (second_split[0].isdigit() or not second_split[0]) and second_split[1] == '':
            if second_split[0].isdigit():
                return 0, int(sign + second_split[0])
            if not second_split[0]:
                return 0, int(sign + "1")
    else:
        return None


def input_number(text, numbers_type):
    if numbers_type == 1:
        try:
            string_number = text.replace(" ", '')
            num = float(string_number)
            return [True, num]
        except ValueError:
            return [False, 0]

    if numbers_type == 2:
        string_number = text.replace(" ", '')
        sign = '-' if string_number[0] == '-' else ''
        if sign == '-':
            string_number = string_number[1:]
        divider = "+"
        if "-" in string_number:
            divider = "-"
        result = numbers_split_and_compere(divider, string_number, sign)
        if result:
            return [True, result]
        else:
            return [False, 0]
