import data_base


def is_exist(name):
    result = data_base.find_by_value('students', 'student_name', name)
    if result:
        return result[0][0]
    else:
        return 0


def add_new_student(name):
    specialization = input("Введите изучаемую специальность: ")
    data_base.add_record('students', {'student_name': name, "study": specialization})
    return data_base.find_by_value('students', 'student_name', name)[0][0]


def show_subjects():
    pass


def submit_homework():
    pass