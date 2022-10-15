import csv
import xml.etree.ElementTree as ElTree

from database import get_all, add_many, find_by_phone, find_by_name


def export_to_csv(file_name):
    data = get_all()
    with open(file_name, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow(item)
    return file_name


def export_to_xml(file_name):
    data = get_all()
    with open(file_name, "w") as xml_file:
        xml_file.write('<?xml version="1.0"?>\n<data>')
        for item in data:
            xml_file.write(f"""
    <id name="{item[0]}">
        <fname>{item[1]}</fname>
        <lname>{item[2]}</lname>
        <phone>{item[3]}</phone>
        <description>{item[4]}</description>
    </id>""")
        xml_file.write('</data>')
    return file_name


def import_from_csv(file_name):
    try:
        with open(file_name, "r", newline='') as csvfile:
            data = csv.reader(csvfile)
            data = list(map(lambda x: x[1:], data))
            new_data = []
            for item in data:
                if not (find_by_name(item[0]) or find_by_phone(item[2])):
                    new_data.append(item)
            add_many(new_data)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден!")
        return False
    return True


def import_from_xml(file_name):
    try:
        tree = ElTree.parse(file_name)
    except FileNotFoundError:
        print(f"Файл {file_name} не найден!")
        return False
    root = tree.getroot()
    data = []
    for child in root:
        # id = child.attrib['name']
        data.append([item.text for item in child])
    new_data = []
    for item in data:
        if not (find_by_name(item[0]) or find_by_phone(item[2])):
            new_data.append(item)
    add_many(new_data)
    add_many(new_data)
    return True
