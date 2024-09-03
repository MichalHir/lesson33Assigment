# from datetime import datetime, timedelta


class User:
    def __init__(self, user_name, number):
        self.name = user_name
        self.number = number
        # self.date_of_loan=None
        print("creating a new user")
    def __str__(self):
        return f"name:{self.name}"
    # def loan_book(self):
    #     if self.date_of_loan is None:
    #         self.date_of_loan = datetime.now()
    #         return_date = self.date_of_loan + timedelta(days=10)
    #         print(f"Return date: {return_date.strftime('%Y-%m-%d %H:%M:%S')}")
    #     else:
    #         print("You already have a book loaned out.")

    # def check_late(self):
    #     if self.date_of_loan:
    #         current_date = datetime.now()
    #         due_date = self.date_of_loan + timedelta(days=10)
    #         if current_date > due_date:
    #             print("YOU ARE LATE. The fine is 50 shekel.")
    #         else:
    #             print("Book is returned on time.")
    #     else:
    #         print("No book is currently loaned.")