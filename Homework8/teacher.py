import data_base


def is_exist(name):
    result = data_base.find_by_value('teachers', 'teacher_name', name)
    if result:
        return result[0][0]
    else:
        return 0


def add_new_teacher(name):
    specialization = input("Введите вашу специализацию: ")
    data_base.add_record('teachers', {'teacher_name': name, "specialization": specialization})
    return data_base.find_by_value('teachers', 'teacher_name', name)[0][0]

