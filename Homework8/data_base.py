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


def get_record_by_value(user_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM marks_table "
                   f"INNER JOIN homeworks ON homeworks.id = marks_table.homework_id "
                   f"WHERE author_id = {user_id};")
    return cursor.fetchall()


def add_many_records(table, records):
    cursor = connection.cursor()
    cursor.executemany(f"INSERT INTO {table}(name, description) VALUES(?, ?);", records)
    connection.commit()
    return records


def find_by_value(table, key, value):
    cursor = connection.cursor()
    cursor.execute(f"select * from {table} where {key}='{value}'")
    return cursor.fetchall()


def del_record_by_value(table, key, value):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE {key}='{value}';")
    connection.commit()
    return value
