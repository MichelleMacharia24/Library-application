from books import Books
from library import Library

library = Library()

book = Books(1, "Python Project", "John Doe", True)

library.new_book(book)

print("Book added successfully.")

library.borrow_book(1)

print("Book borrowed successfully.")

library.return_book(1)

print("Book returned successfully.")

print("Testing complete.")
