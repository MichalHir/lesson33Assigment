from oop_1.book.models import Book
from oop_1.user.models import User


user1 = User("Ran","051-5355555")
user2 = User("Tal","058-5555566")
user3 = User("Gal","054-5555577")

book1=Book("Book1","Author1")
book2=Book("Book2","Author2")
book3=Book("Book3","Author3")
book4=Book("Book4","Author4")
book5=Book("Book5","Author5")

book1.loan_book(user1)
book3.loan_book(user2)
book5.loan_book(user3)

book4.loan_book(user2)