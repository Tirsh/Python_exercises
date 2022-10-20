import data_base
import ui
from loger import log


def show_all_subjects(user_id):
    log(user_id, "show_all_subjects")
    ui.show_records(data_base.get_all_records('subjects'))
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def show_all_hometasks(user_id):
    log(user_id, "show_all_hometasks")
    subjects = data_base.get_all_records('subjects')
    made_hometasks = list(map(lambda x: x[1], data_base.find_by_value('homeworks', 'author_id', user_id)))
    hometasks = list(filter(lambda x: x[0] not in made_hometasks,
                            map(lambda x: [x[0], subjects[x[1]-1][1], x[2]], data_base.get_all_records('hometasks'))))
    if not hometasks:
        print("Для вас нет заданий")
    else:
        ui.show_records(hometasks)
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def add_completed_work(user_id):
    completed_work = ui.new_comleted_work(user_id)
    if not completed_work:
        print("Для вас нет заданий")
        input("Нажмите любую клавишу для возврата в меню.")
        return True
    log(user_id, "add_completed_work")
    data_base.add_record('homeworks', completed_work)
    return True

def show_marked_works(user_id):
    subjects = data_base.get_all_records('subjects')
    marked_works = data_base.get_record_by_value(user_id)
    teachers = data_base.get_all_records("teachers")
    students = data_base.get_all_records("students")
    hometasks = list(map(lambda x: [x[0], subjects[x[1] - 1][1], x[2]], data_base.get_all_records('hometasks')))
    if not marked_works:
        print("У вас нет проверенных работ!")
    else:
        marked_works = list(map(lambda item: [teachers[item[2]-1][1], f"Оценка {item[3]}", item[4],
                            hometasks[item[6]-1], students[item[7]-1][1], item[8]], marked_works))
        ui.show_marked_tasks(marked_works)
    log(user_id, "show_marked_works")
    input("Нажмите любую клавишу для возврата в меню.")
    return True

def add_subject(user_id):
    log(user_id, "add_subject")
    data_base.add_record('subjects', ui.new_subject())
    return True


def add_hometask(user_id):
    # log(f"{user_id}")
    hometask = ui.new_hometask()
    if hometask:
        log(user_id, "add_hometask")
        data_base.add_record('hometasks', hometask)
        return True
    else:
        return False


def show_all_works(user_id):
    evaluate_work = ui.new_mark(user_id)
    if evaluate_work:
        log(user_id, "show_all_works")
        data_base.add_record('marks_table', evaluate_work)
        return True
    else:
        print("Нет выполненных работ")
        input("Нажмите любую клавишу для возврата в меню.")
        return True


def exit_system(user_id):
    log(user_id, "exit_system")
    return False


students_options = {1: show_all_subjects, 2: show_all_hometasks, 3: add_completed_work, 4: show_marked_works, 0: exit_system}
teachers_options = {1: show_all_subjects, 2: add_subject, 3: add_hometask, 4: show_all_works, 0: exit_system}



def start_informational_system():
    data_base.connect_to_base('new_base.db')
    while True:
        user_role, user_id = ui.main_menu()
        if user_role == 0 or user_id == 0:
            print("Работа информационной системы завершена")
            return 0
        run_system = True
        while run_system:
            if user_role == 1:
                option = ui.student_menu()
                run_system = students_options[option](user_id)
            if user_role == 2:
                option = ui.teacher_menu()
                run_system = teachers_options[option](user_id)
