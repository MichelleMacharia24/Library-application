class Library():

    def __init__(self):
        self.books = []
        self.users = []
        self.records = []

    def new_book(self, book):

        """Adds new books into the library."""

        if book not in self.books:
            self.books.append(book)
            print(f"{book.title} has been added to the library.")
        else:
            print("Book is already in the library.")

    def remove_book(self,book):

        """Removes existing books from the library."""

        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the library.")
        else:
            print("Book is not in the library.")

    def borrow_book(self, user, book):

        """Allows users to borrow books from the library."""

        if book in self.books:

            if book.available:
                book.borrow_book()
                user.borrow_book(book)

                print(f"{user.name} has successfully borrowed {book.title}.")

            else:
                print(f"{book.title} has already been borrowed.")
            
        else:
            print("This book is not in the library.")

    def return_book(self, user, book):
         
         """Allows users to return books to the library."""
         
         if book in self.books:
             
             if not book.available:
                book.return_book()
                user.return_book(book)

                print(f"{user.name} has successfully returned {book.title}.")
             
             else:
                print(f"{book.title} is not currently borrowed.")

         else:
            print("This book is not in the library.")

    def search_books(self, title):

        """Allows the user or librarian to search for books by their title."""

        found = False

        for book in self.books:

         if book.title.lower() == title.lower():
            print("Book has been found:")
            book.book_info()
            found = True
            break

        if not found:
            print("Book is not in library.")