import telebot.types
from telebot import TeleBot
import input_checker
import out
from mathematics import make_calc

bot = TeleBot('5649719020:AAGTObnM7A8zDDPgmQ2YrdsKJztJ_tP8oBs')


@bot.message_handler(commands=["menu"])
def show_main_menu(msg: telebot.types.Message):
    menu = """Введите тип чисел.
1. Рациональные
2. Комплексные"""
    bot.send_message(chat_id=msg.from_user.id, text=menu)
    # bot.register_next_step_handler(callback=menu_control, message=msg)


@bot.message_handler()
def menu_control(msg):
    num = msg.text
    text = """Некорректный ввод!
    Введите тип чисел.
    1. Рациональные
    2. Комплексные"""
    if not num.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text=text)
        bot.register_next_step_handler(callback=menu_control, message=msg)
    else:
        if not input_checker.input_type_of_numbers(int(num), {1, 2}):
            bot.send_message(chat_id=msg.from_user.id, text=text)
            bot.register_next_step_handler(callback=menu_control, message=msg)
        else:
            bot.send_message(chat_id=msg.from_user.id, text="Введите действие:")
            bot.register_next_step_handler(callback=input_operation, message=msg, number_type=int(num))


def input_operation(msg, number_type):
    operation = msg.text
    data = []
    if not input_checker.input_operations(operation):
        text = "Некорректный ввод!\nВведите действие:"
        bot.send_message(chat_id=msg.from_user.id, text=text)
        bot.register_next_step_handler(callback=input_operation, message=msg, number_type=number_type)
    else:
        data.append(operation)
        bot.send_message(chat_id=msg.from_user.id, text="Введите первое число:")
        bot.register_next_step_handler(callback=first_number, message=msg, number_type=number_type, data=data)


def first_number(msg, number_type, data):
    number = input_checker.input_number(msg.text, number_type)
    if not number[0]:
        text = "Некорректный ввод!\nВведите первое число:"
        bot.send_message(chat_id=msg.from_user.id, text=text)
        bot.register_next_step_handler(callback=input_operation, message=msg, number_type=number_type)
    else:
        data.append(number[1])
        bot.send_message(chat_id=msg.from_user.id, text="Введите второе число:")
        bot.register_next_step_handler(callback=second_number, message=msg, number_type=number_type, data=data)


def second_number(msg, number_type, data):
    number = input_checker.input_number(msg.text, number_type)
    if not number[0]:
        text = "Некорректный ввод!\nВведите второе число:"
        bot.send_message(chat_id=msg.from_user.id, text=text)
        bot.register_next_step_handler(callback=input_operation, message=msg, number_type=number_type)
    else:
        data.append(number[1])
        result = out.out_result(make_calc(data))
        bot.send_message(chat_id=msg.from_user.id, text=result)
