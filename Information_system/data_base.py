import sqlite3


def connect_to_base(file_name):
    global connection
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       description TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       teacher_name TEXT,
       specialization TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       student_name TEXT,
       study TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS hometasks(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       subject_id INTEGER,
       info TEXT,
       FOREIGN KEY (subject_id) REFERENCES subjects(id));""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS homeworks(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       hometask_id INTEGER,
       author_id INTEGER,
       homework TEXT,
       FOREIGN KEY (author_id) REFERENCES students(id),
       FOREIGN KEY (hometask_id) REFERENCES hometasks(id));""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS marks_table(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       homework_id INTEGER,
       teacher_name_id INTEGER,
       mark INTEGER,
       comment TEXT,
       FOREIGN KEY (teacher_name_id) REFERENCES teachers(id),
       FOREIGN KEY (homework_id) REFERENCES hometasks(id));""")
    connection.commit()
    return 0


def add_record(table, record):
    cursor = connection.cursor()
    keys = record.keys()
    values = [str(record[item]) for item in keys]
    cursor.execute(f"""INSERT INTO {table}({', '.join(keys)}) 
       VALUES({', '.join(map(lambda x: x if x.isdigit() else f"'{x}'", values))});""")
    connection.commit()
    print("Новая запись добавлена")
    return record


def get_all_records(table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table};")
    all_results = cursor.fetchall()
    return all_results


def add_many_records(table, records):
    cursor = connection.cursor()
    cursor.executemany(f"INSERT INTO {table}(name, description) VALUES(?, ?);", records)
    connection.commit()
    return records


def find_by_value(table, key, value):
    cursor = connection.cursor()
    cursor.execute(f"select * from {table} where {key}='{value}'")
    return cursor.fetchall()

# add_record('students', {'student_name': 'Ivanov', "study": 'Разработка ПО'})
# add_record('teachers', {'teacher_name': 'Stepanov', "specialization": 'Программирование JAVA'})
# add_record('subjects', {'name': 'Математика', 'description': 'Начальный курс тригонометрии'})
# add_record('subjects', {'name': 'Химия', 'description': 'Органическая химия'})
#
# print(get_all_records('subjects'))
# add_record('hometasks', {'subject_id': 3, 'info': 'Написать программу учета банковских транзакций'})
# add_record('hometasks', {'subject_id': 1, 'info': 'Решить задания 173-175'})
# add_record('homeworks', {'hometask_id': 2, 'author_id': 1, 'homework': 'Решение задания'})
# add_record('marks_table', {'homework_id': 1, 'teacher_name_id': 1, 'mark': 5, 'comment': "Отличная работа"})
#
# print(get_all_records('teachers'))


