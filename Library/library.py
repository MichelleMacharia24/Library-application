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

    def borrow_book(self, book_id):

        """Allows users to borrow books from the library."""

        for book in self.books:

         if book_id == book.book_id:

            if book.available:
                book.borrow_book()

                print(f"Book has successfully been borrowed.")

            else:
                print(f"{book.title} has already been borrowed.")
            
         else:
            print("This book is not in the library.")

    def return_book(self, book_id):
         
         """Allows users to return books to the library."""

         for book in self.books:
         
          if book_id == book.book_id:
             
             if not book.available:
                book.return_book()

                print(f"Book has successfully been returned.")
             
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