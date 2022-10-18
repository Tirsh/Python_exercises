def write_log(log):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{log}\n")