def create_author_object(first_name, last_name, books):
    return {
        "full_name": lambda: first_name + " " + last_name,
        "is_prolific": lambda: books > 100,
    }

obj = create_author_object("Doni", "Rubiagatra", 500)
print(obj["full_name"]())
