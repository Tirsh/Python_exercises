import sqlite3


def connect_to_base(file_name):
    global connection
    connection = sqlite3.connect(file_name)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS phone_book(
       userid INTEGER PRIMARY KEY AUTOINCREMENT,
       fname TEXT,
       lname TEXT,
       phone TEXT,
       description TEXT);
    """)
    connection.commit()
    return cursor


def get_all():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM phone_book;")
    all_results = cursor.fetchall()
    return all_results


def add_row(new_row):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO phone_book(fname, lname, phone, description) 
       VALUES('{new_row[0]}', '{new_row[1]}', '{new_row[2]}', '{new_row[3]}');""")
    connection.commit()
    print("Новая запись добавлена")
    return new_row


def del_by_name(first_name):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM phone_book WHERE fname='{first_name}';")
    connection.commit()
    return first_name


def find_by_name(first_name):
    cursor = connection.cursor()
    cursor.execute(f"select * from phone_book where fname='{first_name}'")
    return cursor.fetchall()


def find_by_phone(phone):
    cursor = connection.cursor()
    cursor.execute(f"select * from phone_book where phone='{phone}'")
    return cursor.fetchall()


def add_many(numbers):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO phone_book(fname, lname, phone, description) VALUES(?, ?, ?, ?);", numbers)
    connection.commit()
    return numbers
