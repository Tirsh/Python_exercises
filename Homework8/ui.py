import data_base
import student
import teacher
from loger import log


def menu_number_checker(answer, answers):
    return True if answer in answers else False


def input_circle(text, answers):
    while True:
        num = input(text)
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), answers):
            return int(num)
        else:
            print("Некорректный ввод!")


def check_role():
    while True:
        print("""1. Я Студент
2. Я преподаватель
0. Выход""")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if menu_number_checker(int(num), set(range(0, 3))):
            return int(num)
        else:
            print("Некорректный ввод!")


def new_user(role, user_login):
    print("""Пользователь не найден
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
        print(f"Вы зарегистрированы как новый студент, доступ в систему по вашей фамилии: {user_login}!")
        user_id = student.add_new_student(user_login)
        log(user_id, 'add_new_student')
        return user_id
    elif role == 2:
        print(f"Вы зарегистрированы как новый преподаватель, доступ в систему по вашей фамилии: {user_login}!")
        user_id = teacher.add_new_teacher(user_login)
        log(user_id, 'add_new_teacher')
        return user_id


def login(role):
    print("Введите вашу фамилию для входа в информационную систему: ")
    user_login = input("Ваш ввод: ")
    user_id = student.is_exist(user_login) if role == 1 else teacher.is_exist(user_login)
    if user_id != 0:
        return user_id
    else:
        user_id = new_user(role, user_login)
    log(user_id, 'user_login')
    return user_id


def main_menu():

    user_id = 0
    role = 0
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
    if text:
        print(f"\t{record[0]}", end=' ')
        for item in record[1:]:
            print(f"{item} |", end=' ')
        print()
    if not text:
        print(f"\t{record[0]}", end=' ')
        for item in record[1:]:
            print(f"{item} |", end=' ')
        print()
    return record


def show_records(data):
    for item in data:
        show_record(item)
    return data


def show_marked_tasks(data):
    for item, row in enumerate(data):
        show_record([item+1, *row[3][1:]])
        print(f"Выполнил студент: {row[4]}")
        print(f"Работа: {row[5]}")
        print(f"Проверил преподаватель: {row[0]}, оценка {row[1]}, комментарий: {row[2]}")
        print()


def new_subject():
    subject = input("Введите название предмета: ")
    description = input("Введите описание предмета: ")
    return {'name': subject, 'description': description}


def subject_list():
    data = data_base.get_all_records("subjects")
    subjects = list(map(lambda x: x[1], data))
    return subjects


def hometask_list():
    subjects = subject_list()
    data = data_base.get_all_records("hometasks")
    return list(map(lambda record: [record[0], subjects[record[1]-1], record[2]], data))


def homework_list():
    homeworks = hometask_list()
    students = data_base.get_all_records("students")
    data = data_base.get_all_records("homeworks")
    return list(map(lambda record: [record[0], homeworks[record[1]-1], students[record[2]-1][1], record[3]], data))


def new_hometask():
    subjects = subject_list()
    while True:
        for elem, item in enumerate(subjects):
            print(f"{elem+1}. {item}")
        print("0. Выход")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if num == "0":
            return {}
        if menu_number_checker(int(num), set(range(1, len(subjects)+1))):
            num = int(num)
            break
        else:
            print("Некорректный ввод!")
    task = input("Введите задание: ")
    return {'subject_id': num, 'info': task}


def new_comleted_work(user_id):
    made_hometasks = list(map(lambda x: x[1], data_base.find_by_value('homeworks', 'author_id', user_id)))
    hometask = list(filter(lambda x: x[0] not in made_hometasks, hometask_list()))
    if not hometask:
        return {}
    while True:
        for elem, item in enumerate(hometask):
            print(f"{elem+1}. {item[1]}: {item[2]}")
        print("0. Выход")
        num = input("Ваш ввод: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if num == "0":
            return {}
        if menu_number_checker(int(num), set(range(1, len(hometask)+1))):
            num = hometask[int(num)-1][0]
            break
        else:
            print("Некорректный ввод!")
    work = input("Введите решение: ")
    return {'hometask_id': num, 'author_id': user_id, 'homework': work}


def new_mark(user_id):
    marked_works = list(map(lambda x: x[1], data_base.get_all_records("marks_table")))
    work_list = list(filter(lambda x: x[0] not in marked_works, homework_list()))
    if not work_list:
        return {}
    while True:
        for elem, item in enumerate(work_list):
            print(f"{elem+1}. Предмет: {item[1][1]}| Задание: {item[1][2]}")
            print(f"Автор:{item[2]}:\n{item[3]}")
        print("0. Выход")
        num = input("Введите номер работы для оценки: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if num == "0":
            return {}
        if menu_number_checker(int(num), set(range(1, len(work_list)+1))):
            num = work_list[int(num)-1][0]
            break
        else:
            print("Некорректный ввод!")
    mark = input_circle("Оцените работу (2-5): ", set(range(2, 6)))
    comment = input("Введите комментарий к оценке: ")
    return {'homework_id': num, 'teacher_name_id': user_id, 'mark': mark, 'comment': comment}
