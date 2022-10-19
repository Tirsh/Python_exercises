import data_base, ui


def show_all_subjects():
    print(data_base.get_all_records('subjects'))
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def exit_system():
    return False


students_options = {1: show_all_subjects, 0: exit_system}
    # , 2: add_number, 3: find_number, 4: delete_number,
    #        5: make_export, 6: make_import, 7: exit_book}
teachers_options = {1: show_all_subjects, 0: exit_system}
                    # 2: add_number, 3: find_number, 4: delete_number,
#            5: make_export, 6: make_import, 7: exit_book}
def start_informational_system():
    data_base.connect_to_base('new_base.db')
    while True:
        user_role, user_id = ui.main_menu()
        print(user_role)
        print(user_id)
        if user_role == 0 or user_id == 0:
            print("Работа информационной системы завершена")
            return 0
        run_system = True
        while run_system:
            if user_role == 1:
                option = ui.student_menu()
                run_system = students_options[option]()
            if user_role == 2:
                option = ui.teacher_menu()
                run_system = students_options[option]()
