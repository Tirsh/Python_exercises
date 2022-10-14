operation = "2+2*2/4"
operation = operation.replace(" ", "")


def minus(lst):
    return lst[0] - lst[1]


def multi(lst):
    return lst[0] * lst[1]


def divide(lst):
    return lst[0] / lst[1]


def count_from_string(operation):
    if "(" in operation:
        bk1 = operation.rindex("(")
        bk2 = operation.index(")", bk1)
        return count_from_string(operation[:bk1] + str(count_from_string(operation[bk1 + 1:bk2])) + operation[bk2 + 1:])
    if operation.isdigit():
        return int(operation)
    if "+" in operation:
        return sum([count_from_string(item) for item in operation.split("+", 1)])
    if "-" in operation:
        return minus([count_from_string(item) for item in operation.split("-", 1)])
    if "/" in operation:
        return divide([count_from_string(item) for item in operation.split("/", 1)])
    if "*" in operation:
        return multi([count_from_string(item) for item in operation.split("*", 1)])


print(count_from_string(operation))
