# loan_book(user), return_book()
class Book:
    def __init__(self, name, author, user):
        self.name = name
        self.author = author
        self.user = user
        print("creating a new book")

    def __str__(self):
        return f"name:{self.name}"
    
    # def loan_book(self,user):

    # def return_book(self):

