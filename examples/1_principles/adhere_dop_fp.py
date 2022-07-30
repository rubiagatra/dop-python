def create_author_object(first_name, last_name, books):
    return {
        "first_name": first_name, 
        "last_name": last_name,
        "books": books
    }

def full_name(data):
    return data.first_name + " " + data.last_name

def is_prolific(data):
   return data.books > 100

obj = create_author_object("Doni", "Rubiagatra", 500)
print(full_name(obj))
