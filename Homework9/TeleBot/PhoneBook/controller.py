import database
import import_export
import out

DATA_BASE = "tel.db"


def show_all_numbers():
    return out.show_records(database.get_all())


def add_number(data):
    new_number = data
    if not is_exist(new_number):
        database.add_row(new_number)
        return "Запись добавлена"
    else:
        return "Запись с таким номером есть!"


def is_exist(record):
    return database.find_by_name(record[0]) or database.find_by_phone(record[2])


def find_number(data):
    result = database.find_by_name(data[0])
    if result:
        return out.show_records(result)
    else:
        return "Запись не найдена"


def delete_number(data):
    database.del_by_name(data[0])
    return "Готово"


def make_export(data):
    file = data[0]
    option = data[1]
    if option == 1:
        import_export.export_to_csv(file)
    elif option == 2:
        import_export.export_to_xml(file)
    return f"Выполнен экспорт в {file}"


def make_import(data):
    file = data[0]
    option = data[1]
    success = False
    if option == 1:
        success = import_export.import_from_csv(file)
    elif option == 2:
        success = import_export.import_from_xml(file)
    if success:
        return f"Выполнен импорт из {file}"


options = {1: show_all_numbers, 2: add_number, 3: find_number, 4: delete_number,
           5: make_export, 6: make_import}


def start_from_bot(option, data):
    database.connect_to_base(DATA_BASE)
    if data:
        result = options[option](data)
    else:
        result = options[option]()
    return result
