class Author:
    def __init__(self, first_name, last_name, books):
        self.first_name = first_name
        self.last_name = last_name 
        self.books = books 

    def full_name(self):
        return self.first_name + " " + self.last_name

    def is_prolific(self):
        return self.books > 100

obj = Author("Doni", "Rubiagatra", 500)
obj.full_name()
        