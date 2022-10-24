import telebot.types
from telebot import TeleBot
from controller import start_from_bot


bot = TeleBot('5649719020:AAGTObnM7A8zDDPgmQ2YrdsKJztJ_tP8oBs')


def add_new_number(msg, option):
    data = msg.text.split()
    result = start_from_bot(option, data)
    bot.send_message(chat_id=msg.from_user.id, text=result)


def find_and_del(msg, option):
    data = msg.text.split()
    result = start_from_bot(option, data)
    bot.send_message(chat_id=msg.from_user.id, text=result)


def menu_number_checker(answer, answers):
    return True if answer in answers else False


def export_and_import_menu(msg, option):
    num = msg.text
    if not num.isdigit() and menu_number_checker(num, set(range(1, 3))):
        bot.send_message(chat_id=msg.from_user.id, text="Некорректный ввод!")
        bot.register_next_step_handler(callback=export_and_import_menu, message=msg, option=option)
    else:
        num = int(num)
        file = "CSV" if num == 1 else "XML"
        if option == 5:
            bot.send_message(chat_id=msg.from_user.id, text=f"Введите имя {file} файла: ")
        else:
            bot.send_message(chat_id=msg.from_user.id, text=f"Загрузите {file} файл: ")
        bot.register_next_step_handler(callback=file_export_and_import, message=msg, option=option, file_type=num)


@bot.message_handler(content_types=['document'])
def file_export_and_import(msg, option, file_type):
    if option == 5:
        file = msg.text
        result = start_from_bot(option, [file, file_type])
        bot.send_message(chat_id=msg.from_user.id, text=result)
        bot.send_document(chat_id=msg.from_user.id, document=open(file, 'rb'))
    else:
        file = bot.get_file(msg.document.file_id)
        downloaded_file = bot.download_file(file.file_path)
        src = msg.document.file_name
        with open(src, 'wb') as f_out:
            f_out.write(downloaded_file)
        result = start_from_bot(option, [src, file_type])
        bot.send_message(chat_id=msg.from_user.id, text=result)


@bot.message_handler(commands=['help'])
def show_help(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="/menu - чтобы увидеть меню")


@bot.message_handler(commands=['menu'])
def show_main_menu(msg: telebot.types.Message):
    menu = """1. Просмотр записей
2. Добавление записи
3. Поиск записи
4. Удаление записи
5. Экспорт
6. Импорт """
    bot.send_message(chat_id=msg.from_user.id, text=menu)
    bot.register_next_step_handler(callback=menu_control, message=msg)


@bot.message_handler()
def menu_control(msg):
    user_id = msg.from_user.id
    num = msg.text
    if not num.isdigit():
        bot.send_message(chat_id=msg.from_user.id, text="Некорректный ввод!")
    else:
        num = int(num)
        if menu_number_checker(num, set(range(1, 8))):
            data = []
            if num == 2:
                bot.send_message(chat_id=user_id, text="Введите: ФАМИЛИЯ ИМЯ ТЕЛЕФОН ОПИСАНИЕ")
                bot.register_next_step_handler(callback=add_new_number, message=msg, option=num)
            elif num == 3 or num == 4:
                action = "удаления" if num == 4 else "поиска"
                bot.send_message(chat_id=user_id, text=f"Введите фамилию для {action}:")
                bot.register_next_step_handler(callback=find_and_del, message=msg, option=num)
            elif num == 5 or num == 6:
                operation = "Экспорт" if num == 5 else "Импорт"
                text = f"""1. {operation} в CSV
2. {operation} XML """
                bot.send_message(chat_id=user_id, text=text)
                bot.register_next_step_handler(callback=export_and_import_menu, message=msg, option=num)
            else:
                result = start_from_bot(num, data)
                if result:
                    bot.send_message(chat_id=user_id, text=result)
                else:
                    bot.send_message(chat_id=user_id, text="Записей нет")
        else:
            bot.send_message(chat_id=user_id, text="Некорректный ввод!")
