from datetime import datetime


def write_log(log):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{dt_string} : {log}\n")
