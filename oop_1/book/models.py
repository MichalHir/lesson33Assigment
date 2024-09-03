from datetime import datetime, timedelta
class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.user = None
        self.loan_date= None
        print("creating a new book")

    def __str__(self):
        return f"name:{self.name}"

    def loan_book(self, user):
        # if self.user is None:
        #     self.user = user
        #     user.loan_book()
        # else:
        #     print("Book is already loaned out.")
        self.user = user 
        self.loan_date= datetime.today()
        print("RETURN BY ",self.loan_date+timedelta(days=10))
    def return_book(self,date_of_return):
        if not date_of_return:
            date_of_return = datetime.today()
        if not date_of_return>self.loan_date+timedelta(days=10):
            print("50 shekels fine")
        print(f"{self.name} was returned by {self.user}")
        self.user = None
        self.loan_date=None

    # def return_book(self, user):
    #     if self.user == user:
    #         self.user.check_late()
    #         self.user = None
    #         user.date_of_loan = None
    #     else:
    #         print("This book was not loaned to you.")
