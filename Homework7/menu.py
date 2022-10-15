def show_menu():
    while True:
        num = input("""        1. Просмотр записей
        2. Добавление записи
        3. Поиск записи
        4. Удаление записи
        5. Экспорт
        6. Импорт
        7. Выход
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
        3. Выход
        """)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(1, 4))):
            return int(num)
        else:
            print("Некорректный ввод!")


def show_import_menu():
    while True:
        num = input("""        1. Импорт из CSV
        2. Импорт из XML
        3. Выход
        """)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(1, 4))):
            return int(num)
        else:
            print("Некорректный ввод!")


def show_record(record, text=''):
    if not text:
        print(f"ID: {record[0]}| Фамилия: {record[1]}, Имя: {record[2]}, Тел.: {record[3]}, Комментарий: {record[4]}")
    if text:
        print(text)
        print(f"ID: {record[0]}| Фамилия: {record[1]}, Имя: {record[2]}, Тел.: {record[3]}, Комментарий: {record[4]}")
    return record


def show_records(data):
    for item in data:
        show_record(item)
    return data


def new_number():
    first_name = input_not_null("Ведите фамилию: ")
    second_name = input_not_null("Введите имя: ")
    phone = input_not_null("Введите телефон: ")
    description = input_not_null("Введите описание: ")
    return first_name, second_name, phone, description


def get_first_name():
    first_name = input_not_null("Ведите фамилию: ")
    return first_name


def get_file_name():
    file_name = input_not_null("Введите имя и путь к файлу: ")
    return file_name


def input_not_null(text):
    while True:
        new_string = input(text)
        if new_string:
            return new_string
        else:
            print("Введена пустая строка!")
