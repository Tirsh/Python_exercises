import database
import import_export
import Menu

DATA_BASE = "tel.db"


def show_all_numbers():
    Menu.show_records(database.get_all())
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def add_number():
    new_number = Menu.new_number()
    if not is_exist(new_number):
        database.add_row(new_number)
    else:
        print("Запись с таким номером есть!")
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def is_exist(record):
    return database.find_by_name(record[0]) or database.find_by_phone(record[2])


def find_number():
    result = database.find_by_name(Menu.get_first_name())
    if result:
        Menu.show_records(result)
    else:
        print("Запись не найдена")
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def delete_number():
    database.del_by_name(Menu.get_first_name())
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def make_export():
    file = ""
    option = Menu.show_export_menu()
    if option == 1:
        file = Menu.get_file_name()
        import_export.export_to_csv(file)
    elif option == 2:
        file = Menu.get_file_name()
        import_export.export_to_xml(file)
    elif option == 3:
        input("Нажмите любую клавишу для возврата в меню.")
        return True
    print(f"Выполнен экспорт в {file}")
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def make_import():
    file = ""
    option = Menu.show_import_menu()
    success = False
    if option == 1:
        file = Menu.get_file_name()
        success = import_export.import_from_csv(file)
    elif option == 2:
        file = Menu.get_file_name()
        success = import_export.import_from_xml(file)
    elif option == 3:
        input("Нажмите любую клавишу для возврата в меню.")
        return True
    if success:
        print(f"Выполнен импорт из {file}")
    input("Нажмите любую клавишу для возврата в меню.")
    return True


def exit_book():
    return False


options = {1: show_all_numbers, 2: add_number, 3: find_number, 4: delete_number,
           5: make_export, 6: make_import, 7: exit_book}


def start_phone_book():
    database.connect_to_base(DATA_BASE)
    continue_to_work = True
    while continue_to_work:
        option = Menu.show_menu()
        continue_to_work = options[option]()
    return 0
