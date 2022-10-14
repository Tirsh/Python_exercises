def show_menu():
    while True:
        num = input("""        1. Просмотр записей
        2. Добавление записи
        3. Поиск записи
        4. Удаление записи
        5. Экспорт (не менее двух форматов)
        6. Импорт (не менее двух форматов)
        7. Выход из программы (программа должна работать, пока пользователь сам не выйдет из неё)
        """)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(1, 8))):
            return int(num)
        else:
            print("Некорректный ввод!")


def menu_number_checker(answer, answers):
    return True if answer in answers else False


def show_export_menu():
    while True:
        num = input("""        1. Экспорт в CSV
        2. Экспорт в XML
        3. Выход)
        """)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(1, 4))):
            return int(num)
        else:
            print("Некорректный ввод!")


print(show_export_menu())

