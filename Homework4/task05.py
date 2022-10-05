def read_polinom_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


DEGREES = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}


def int_to_degree(num):
    if num <= 1:
        return ""
    if num < 10:
        return DEGREES[num]
    return f"{DEGREES[num // 10]}{DEGREES[num % 10]}"


def get_number_from_degree(degree):
    length = len(degree)
    result = 0
    for i in range(length):
        for key, value in DEGREES.items():
            if degree[i] == value:
                result += 10 ** (length - 1 - i) * key
    if degree == '':
        result = 1
    return result


def create_polinom_dict(line):
    polinom_dict = {}
    minus = False
    for item in line.split():
        member = item.split('x')
        if '+' in member:
            minus = False
            continue
        elif '-' in member:
            minus = True
            continue
        elif '=' in member or '0' in member:
            continue
        if member[0] == '':
            member[0] = 1
        polinom_dict[get_number_from_degree(member[-1])] = int(member[0]) if not minus else -(int(member[0]))
    return polinom_dict


def sum_polinoms(pol1, pol2):
    sum_dict = {}
    max_grade = max(pol1) if max(pol1) > max(pol2) else max(pol2)
    for i in range(max_grade + 1):
        if i in pol1 and i in pol2:
            sum_dict[i] = pol1[i] + pol2[i]
        elif i in pol1 and i not in pol2:
            sum_dict[i] = pol1[i]
        elif i in pol2 and i not in pol1:
            sum_dict[i] = pol2[i]
        else:
            sum_dict[i] = 0
    return sum_dict


def create_polinom_string(polinom_dict):
    max_grade = max(polinom_dict)
    result_list = []
    for i in range(max_grade + 1):
        if polinom_dict[i] != 0 and i != 0:
            result_list.append(f"{abs(polinom_dict[i])}x{int_to_degree(i)}")
        elif polinom_dict[i] != 0 and i == 0:
            result_list.append(f"{abs(polinom_dict[i])}")
        if polinom_dict[i] != 0:
            if polinom_dict[i] > 0:
                result_list.append('+')
            else:
                result_list.append('-')
    return str.join(' ', reversed(result_list)) + ' = 0'


readed_line = read_polinom_from_file('polinom1.txt')
polinom1 = create_polinom_dict(readed_line)
readed_line = read_polinom_from_file('polinom2.txt')
polinom2 = create_polinom_dict(readed_line)
polinoms_sum = (sum_polinoms(polinom1, polinom2))
polinoms_sum_str = create_polinom_string(polinoms_sum)
with open("polinoms_sum.txt", 'w', encoding="utf-8") as f:
    f.write(polinoms_sum_str)
