def log(user_id, text):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{user_id:} {text}\n")
