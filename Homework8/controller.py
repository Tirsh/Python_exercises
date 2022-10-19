import data_base, ui


def show_all_subjects(user_id):
    # log(f"{user_id}")
    print(data_base.get_all_records('subjects'))
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def show_all_hometasks(user_id):
    # log(f"{user_id}")
    print(data_base.get_all_records('hometasks'))
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def add_completed_work(user_id):
    # log(f"{user_id}")
    completed_work = ui.new_comleted_work(user_id)
    data_base.add_record('homeworks', completed_work)
    return True

def show_marked_works(user_id):
    marked_works = data_base.get_record_by_value(user_id)
    if not marked_works:
        print("У вас нет проверенных работ!")
    return True

def add_subject(user_id):
    # log(f"{user_id}")
    data_base.add_record('subjects', ui.new_subject())
    return True


def add_hometask(user_id):
    # log(f"{user_id}")
    hometask = ui.new_hometask()
    if hometask:
        data_base.add_record('hometasks', hometask)
        return True
    else:
        return False


def show_all_works(user_id):
    evaluate_work = ui.new_mark(user_id)
    if evaluate_work:
        data_base.add_record('marks_table', evaluate_work)
        return True
    else:
        return False


def exit_system(user_id):
    # log(f"{user_id}")
    return False


students_options = {1: show_all_subjects, 2: show_all_hometasks, 3: add_completed_work, 4: show_marked_works, 0: exit_system}
    # 3: add_completed_work, 4: show_marked_works,
    #        5: make_export, 6: make_import, 7: exit_book}
teachers_options = {1: show_all_subjects, 2: add_subject, 3: add_hometask, 4: show_all_works, 0: exit_system}
                    #  4: show_all_works,
#            5: make_export, 6: make_import, 7: exit_book}


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
