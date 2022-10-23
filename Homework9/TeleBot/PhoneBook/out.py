def menu_number_checker(answer, answers):
    return True if answer in answers else False


def show_record(record, text=''):
    if not text:
        return f"ID: {record[0]}| Фамилия: {record[1]}, Имя: {record[2]}, Тел.: {record[3]}, Комментарий: {record[4]}"
    if text:
        return f"{text}\nID: {record[0]}| Фамилия: {record[1]}, Имя: {record[2]}, Тел.: {record[3]}, Комментарий: {record[4]}"


def show_records(data):
    message =''
    for item in data:
        message += f"{item}\n"
    return message
