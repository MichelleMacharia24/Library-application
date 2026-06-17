from users import Users
from books import Books
from borrowed import Borrowed

user1 = Users(1, "Alice Wonder", "alicewonder@python.com")

book1 = Books(101, "Python Rocks", "John Doe", True)
book2 = Books(102, "Data Structures", "Jazz King", True)

user1.borrow_book(book1)
user1.borrow_book(book2)

user1.user_info()


record1 = Borrowed(1,50,101)
record1.new_record("20/06/2026")
record1.close_record("01/02/2027")

record1.record_info()
print(record1.check_returned())
