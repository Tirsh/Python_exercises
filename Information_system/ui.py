import teacher, student
def menu_number_checker(answer, answers):
    return True if answer in answers else False


def check_role():
    while True:
        print("""1. Я Студент
2. Я предподаватель
0. Выход""")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(0, 3))):
            return int(num)
        else:
            print("Некорректный ввод!")


def new_user(role, login):
    print("""Позьзователь не найден
Для регистрации в системе подтвердите регистрацию""")
    while True:
        num = input("""1. Подтвердить регистрацию
2. Не регистрироваться
Ваш ввод: """)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(1, 3))):
            num = int(num)
            break
        else:
            print("Некорректный ввод!")
    if num == 2:
        return 0
    if role == 1:
        print(f"Вы зарегистрированы как новый студент, доступ в систему по вашей фамилии: {login}!")
        return student.add_new_student(login)
    elif role == 2:
        print(f"Вы зарегистрированы как новый предподаватель, доступ в систему по вашей фамилии: {login}!")
        return teacher.add_new_teacher(login)


def login(role):
    print("Введите вашу фамилию для входа в информационную систему: ")
    login = input("Ваш ввод: ")
    id = student.is_exist(login) if role == 1 else teacher.is_exist(login)
    if id != 0:
        return id
    else:
        id = new_user(role, login)
    return id


def main_menu():
    user_id = 0
    while user_id == 0:
        print("Вас приветствует информационный портал обучающего центра \"Лютик\"")
        print("Выберете пункт меню:")
        role = check_role()
        if role == 0:
            return 0, 0
        user_id = login(role)
    return role, user_id


def teacher_menu():
    while True:
        print("""    1. Вывести список предметов
    2. Добавить предмет
    3. Добавить домашнее задание
    4. Просмотреть список выполненных работ
    0. Выход""")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(0, 5))):
            return int(num)
        else:
            print("Некорректный ввод!")
    pass


def student_menu():
    while True:
        print("""    1. Вывести список предметов
    2. Вывести список домашних заданий
    3. Сдать работу на проверку
    4. Просмотр оцененных работ
    0. Выход""")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(0, 5))):
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