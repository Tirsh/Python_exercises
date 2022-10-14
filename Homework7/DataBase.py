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


def show_all():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM phone_book;")
    all_results = cursor.fetchall()
    print(all_results)
    return all_results


def add_number(tel_dict):
    cursor = connection.cursor()
    cursor.execute(f"""INSERT INTO phone_book(fname, lname, phone, description) 
       VALUES('{tel_dict["fname"]}', '{tel_dict["lname"]}', '{tel_dict["phone"]}', '{tel_dict["description"]}');""")
    connection.commit()
    return tel_dict


def del_by_name(first_name):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM phone_book WHERE fname='{first_name}';")
    connection.commit()
    return first_name


def find_by_name(first_name):
    cursor = connection.cursor()
    cursor.execute(f"select * from phone_book where fname='{first_name}'")
    print(cursor.fetchall())
    return first_name


def find_by_phone(phone):
    cursor = connection.cursor()
    cursor.execute(f"select * from phone_book where fname='{phone}'")
    print(cursor.fetchall())
    return phone


def add_many(numbers):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO phone_book VALUES(?, ?, ?, ?, ?);", numbers)
    connection.commit()
    return numbers


connect_to_base("tel.db")
add_number({"fname": "Vasipov", "lname": "Vasleriy", "phone": "+79112110012", "description": "Nothing special"})
show_all()
# del_by_name("Vasipov")
show_all()
find_by_name("Berg")