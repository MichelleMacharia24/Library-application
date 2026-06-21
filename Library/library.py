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

                print(f"{user.name} has successfully borrowed {book.title}")

            else:
                print(f"{book.title} has already been borrowed.")
            
        else:
            print("This book is not in the library.")