import random

FIELD_MAP = {0: 11, 1: 21, 2: 31, 3: 12, 4: 22, 5: 32, 6: 13, 7: 23, 8: 33}


def input_int(text, answers):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            num = int(text_in)
            if num not in answers:
                print("Допустимые ходы {}".format(answers))
                continue
            return int(text_in)
        else:
            print("Некорректный ввод!")


def draw_field(field):
    desk = {None: " ", True: "X", False: "0"}
    print("""
               1   2   3
            1  {} | {} | {}
              -----------
            2  {} | {} | {}
              -----------
            3  {} | {} | {}""".format(*[desk[i] for i in field]))


def move_to_field(move):
    for key, item in FIELD_MAP.items():
        if item == move:
            return key


def available_moves(field):
    return {FIELD_MAP[item] for item in range(len(field)) if field[item] is None}


def make_move(field):
    moves_set = available_moves(field)
    return input_int("Сделайте ход в формате XY: ", moves_set)


def bot_move(field):
    test_field = field.copy()
    max_priority = {11, 31, 22, 13, 33}
    moves_set = available_moves(field)
    for item in moves_set:
        test_field[move_to_field(item)] = False
        if check_winner(test_field):
            return item
        test_field[move_to_field(item)] = None
    for item in moves_set:
        test_field[move_to_field(item)] = True
        if check_winner(test_field):
            return item
        test_field[move_to_field(item)] = None
    if 22 in moves_set:
        return 22
    if not max_priority.isdisjoint(moves_set):
        return random.choice(tuple(max_priority & moves_set))
    return random.choice(tuple(moves_set))


def lottery():
    result = random.randrange(1, 3)
    print("Проведена жеребьевка, первым ходит {}".format({1: "Игрок", 2: "Бот"}[result]))
    return True if result == 1 else False


def formed_a_line(line):
    if line.count(False) == 3 or line.count(True) == 3:
        return True
    return False


def check_winner(field):
    for i in range(3):
        if formed_a_line(field[i * 3:i * 3 + 3]):
            return True
        if formed_a_line(field[i::3]):
            return True
    if formed_a_line(field[0::4]) or formed_a_line(field[2:7:2]):
        return True
    return False


def start_game():
    game_over = False
    winner = 0
    field = [None for _ in range(9)]
    print("Игрок: Х")
    print("Бот:   0")
    input("Для начала игры нажмите [ENTER]")
    first_turn = lottery()
    if first_turn:
        draw_field(field)
    while not game_over:
        if first_turn:
            print("\nХод Игрока: ")
            move = make_move(field)
            field[move_to_field(move)] = True
            draw_field(field)
            game_over = check_winner(field)
            winner = 1 if game_over else 0
            first_turn = False
        else:
            print("\nХод Бота: ")
            move = bot_move(field)
            field[move_to_field(move)] = False
            draw_field(field)
            game_over = check_winner(field)
            winner = 2 if game_over else 0
            first_turn = True
        if None not in field:
            game_over = True
    winners = {0: "Ничья!", 1: "Побеждает игрок!", 2: "Побеждает Бот!"}
    print("Конец игры!\n{}".format(winners[winner]))


start_game()
