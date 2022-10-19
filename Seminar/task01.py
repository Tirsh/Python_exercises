operation = "(2+2)*2/4"
operation = operation.replace(" ", "")


def minus(lst):
    return lst[0] - lst[1]


def multi(lst):
    return lst[0] * lst[1]


def divide(lst):
    return lst[0] / lst[1]


def count_from_string(oper):
    if "(" in oper:
        bk1 = oper.rindex("(")
        bk2 = oper.index(")", bk1)
        return count_from_string(oper[:bk1] + str(count_from_string(oper[bk1 + 1:bk2])) + oper[bk2 + 1:])
    if oper.isdigit():
        return int(oper)
    if "+" in oper:
        return sum([count_from_string(item) for item in oper.split("+", 1)])
    if "-" in oper:
        return minus([count_from_string(item) for item in oper.split("-", 1)])
    if "/" in oper:
        return divide([count_from_string(item) for item in oper.split("/", 1)])
    if "*" in oper:
        return multi([count_from_string(item) for item in oper.split("*", 1)])


print(count_from_string(operation))
