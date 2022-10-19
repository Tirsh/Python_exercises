import teacher, student, data_base
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
    return list(map(lambda record: [homeworks[record[1]-1], students[record[2]-1][1], record[3]], data))



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
    hometask = hometask_list()
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
            num = int(num)
            break
        else:
            print("Некорректный ввод!")
    work = input("Введите решение: ")
    return {'hometask_id': num, 'author_id': user_id, 'homework': work}


def new_mark(user_id):
    work_list = homework_list()
    while True:
        for elem, item in enumerate(work_list):
            print(f"{elem+1}. Предмет: {item[0][1]}| Задание: {item[0][2]}")
            print(f"Автор:{item[1]}:\n{item[2]}")
        print("0. Выход")
        num = input("Введите номер работы для оценки: ")
        if not num.isdigit():
            print("Некорректный ввод!")
            continue
        if num == "0":
            return {}
        if menu_number_checker(int(num), set(range(1, len(work_list)+1))):
            num = int(num)
            break
        else:
            print("Некорректный ввод!")
    mark = input_circle("Оцените работу (2-5): ", set(range(2, 6)))
    comment = input("Введите комментарий к оценке: ")
    return {'homework_id': num, 'teacher_name_id': user_id, 'mark': mark, 'comment': comment}




