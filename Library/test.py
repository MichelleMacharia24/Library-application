from users import Users
from books import Books

user1 = Users(1, "Alice Wonder", "alicewonder@python.com")

book1 = Books(101, "Python Rocks", "John Doe", True)
book2 = Books(102, "Data Structures", "Jazz King", True)

user1.borrow_book(book1)
user1.borrow_book(book2)

user1.user_info()