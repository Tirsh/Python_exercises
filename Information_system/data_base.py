import sqlite3


def connect_to_base(file_name):
    global connection
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS subjects(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       description TEXT);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS hometasks(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       subject_id INTEGER,
       info TEXT,
       FOREIGN KEY (subject_id) REFERENCES subjects(id));""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS homeworks(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       hometask_id INTEGER,
       author TEXT,
       homework TEXT,
       FOREIGN KEY (hometask_id) REFERENCES hometasks(id));""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS marks_table(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       homework_id INTEGER,
       teacher_name TEXT,
       mark INTEGER,
       comment TEXT,
       FOREIGN KEY (homework_id) REFERENCES hometasks(id));""")
    connection.commit()
    return 0


def add_subject(new_row):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO subjects(name, description) 
       VALUES('{new_row[0]}', '{new_row[1]}');""")
    connection.commit()
    print("Новая запись добавлена")
    return new_row


def add_many_subjects(subjects):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO subjects(name, description) VALUES(?, ?);", subjects)
    connection.commit()
    return subjects

def add_hometask(new_task):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO hometasks(subject_id, info) 
       VALUES({new_task[0]}, '{new_task[1]}');""")
    connection.commit()
    print("Новая запись добавлена")
    return new_task


def add_homework(new_homework):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO homeworks(hometask_id, author, homework) 
       VALUES({new_homework[0]}, '{new_homework[1]}', '{new_homework[2]}');""")
    connection.commit()
    print("Новая запись добавлена")
    return new_homework


def add_mark(new_mark):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO marks_table(homework_id, teacher_name, mark, comment) 
       VALUES({new_mark[0]}, '{new_mark[1]}', {new_mark[2]}, '{new_mark[3]}');""")
    connection.commit()
    print("Новая запись добавлена")
    return new_mark


def get_all_subjects():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM subjects;")
    all_results = cursor.fetchall()
    return all_results


def get_all_hometasks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM hometasks;")
    all_results = cursor.fetchall()
    return all_results


def get_all_homeworks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM homeworks;")
    all_results = cursor.fetchall()
    return all_results
def get_all_marks():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM marks_table;")
    all_results = cursor.fetchall()
    return all_results


connect_to_base('new_base.db')
# add_subject(['Математика', 'Начальный курс тригонометрии'])
# add_subject(['Химия', 'Органическая химия'])
# add_subject(['Программирование', 'Java, Spring, Hibernate'])
# print(get_all_subjects())

# add_hometask([3, 'Написать программу учета банковских транзакций'])
# add_hometask([1, 'Решить задания 173-175'])
# print(get_all_hometasks())
# add_homework([2, "Petrov", "Решение задания"])
# print(get_all_homeworks())
# add_mark([1, "Varenikov", 5, "Отличная работа"])
print(get_all_marks())
