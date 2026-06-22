from books import Books
from library import Library
from data_manager import save_books

library = Library()

book1 = Books(101, "Python Rocks", "John Doe")
book2 = Books(102, "Data Structures", "Jane Smith")
book3 = Books(103, "Algorithms", "Alan Brown")

library.new_book(book1)
library.new_book(book2)
library.new_book(book3)

print("\nDEBUG: Library contents:")
for b in library.books:
    print(b.title)

save_books(library.books)

print("\nSaved to CSV")

from data_manager import load_books

books = load_books()

print("Books loaded from file:\n")

for book in books:
    print(book.book_id, book.title, book.author, book.available)


from data_manager import save_users, load_users
from users import Users

u1 = Users(1, "Alice", "alice@email.com")

users = [u1]

save_users(users)

loaded = load_users()

for u in loaded:
    print(u.user_id, u.name, u.email)

from data_manager import save_records, load_records
from borrowed import Borrowed

r1 = Borrowed(1, 1, 101)
r1.new_record("2026-01-01")

records = [r1]

save_records(records)

loaded = load_records()

for r in loaded:
    print(r.record_id, r.user_id, r.book_id)