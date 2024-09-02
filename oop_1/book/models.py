# loan_book(user), return_book()
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.user = None
        print("creating a new book")

    def __str__(self):
        return f"name:{self.name}"
    
    def loan_book(self,user):
        if self.user is None:
            self.user = user
            user.loan_book()
        else:
            print("Book is already loaned out.")

    def return_book(self):
        print(f"{self.name} was returned by {self.user}")
        self.user = None
    # def return_book(self, user):
    #     if self.user == user:
    #         self.user.check_late()
    #         self.user = None
    #         user.date_of_loan = None
    #     else:
    #         print("This book was not loaned to you.")

