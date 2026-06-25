from books import Books
from library import Library
from data_manager import save_books, load_books

library = Library()
library.books = load_books("Library/books.csv")

while True:
    print("======LIBRARY======")
    print("1. View all books.")
    print("2. Add a book.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Save and exit.")

    option = input("Kindly enter your choice: ")

    if option == "1":
        print("--- ALL BOOKS ---")
        for book in library.books:
            print(book.book_id, book.title, book.author, book.available)

    elif option == "2":
        print("--- ADD NEW BOOK ---")

        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        new_book = Books(book_id, title, author)

        library.new_book(new_book)

        print(f"{title} has been added successfully!")
        
    elif option == "3":
        print("--- BORROW A BOOK ---")

        try:
            book_id = int(input("Enter book ID: "))
            library.borrow_book(book_id)

        except ValueError:
            print("Please enter a valid book ID.")


    elif option == "4":
        print ("--- RETURN A BOOK ---")

        try:
            book_id = int(input("Enter book ID: "))
            library.return_book(book_id)
        
        except ValueError:
            print("Please enter a valid book ID.")
    
    elif option == "5":
        save_books(library.books)
        print("Books saved.")
        break

