import random

CANDIES = 2021


def input_int(text, answers):
    # Функция ввода целого числа
    while True:
        text_in = input(text)
        if text_in.isdigit():
            num = int(text_in)
            if num not in answers:
                print("Необходимо ввести число в диапазоне {} - {}".format(min(answers), max(answers)))
                continue
            return int(text_in)
        else:
            print("Некорректный ввод!")


def choice_game_type():
    return input_int("Введите тип игры: \n 1. Против человека.\n 2. Против бота \n Ответ: ", {1, 2})


def play_vs_man(candies):
    answer = 28 if candies > 28 else candies
    turn = input_int("Осталось {} конфет, сделайте ход: ".format(candies), set(range(1, answer + 1)))
    return turn


def play_vs_bot(candies):
    if candies <= 28:
        return candies
    best_answer = candies - (candies // 28) * 28 - 1
    turn = best_answer if best_answer != 0 else random.randrange(1, 29)
    print("Осталось {} конфет, бот сделал ход: {}".format(candies, turn))
    return turn


def lottery():
    result = random.randrange(1, 3)
    print("Проведена жеребьевка, первым ходит игрок {}".format(result))
    return True if result == 1 else False


def start_game(candies, first_player, second_player):
    first_turn = lottery()
    game_over = False
    winner = 0
    while not game_over:
        if candies > 0:
            if first_turn:
                print("\nХод первого игрока: ")
                candies -= first_player(candies)
                winner = 1 if candies == 0 else 0
                first_turn = False
            else:
                print("\nХод второго игрока: ")
                candies -= second_player(candies)
                winner = 2 if candies == 0 else 0
                first_turn = True
        else:
            game_over = True
            print('Выиграл {} игрок!!!'.format(winner))


game_type = {1: play_vs_man, 2: play_vs_bot}
start_game(CANDIES, play_vs_man, game_type[choice_game_type()])
