class Author:
    def __init__(self, first_name, last_name, books):
        self.first_name = first_name
        self.last_name = last_name 
        self.books = books 


class NameCalculation:
    @staticmethod
    def full_name(data):
        return data.first_name + " " + data.last_name

class AuthorRationg:
    @staticmethod
    def is_prolific(data):
        return data.books > 100


obj = Author("Doni", "Rubiagatra", 500)
print(NameCalculation.full_name(obj))
