class Books():

    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def book_info(self):

        """Displays the information about the book."""

        print(f"Book ID: {self.book_id}\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Availability: {self.available}")
        

    def book_borrowed(self):

        """Marks a book as borrowed."""

        if self.available == True:
            print(f"{self.title} is available")
        else:
            print(f"{self.title} is already borrowed.")

    def book_returned(self):

        """Marks a book as returned."""

        if self.available == True:
            print(f"{self.title} has been returned.")

    def update_book(self, new_title, new_author):

        """Updates the details of an exisiting book."""

        self.title = new_title
        self.author = new_author

        print("Book details updated.")


book1 = Books(10, "Python rules", "Michelle Macharia", True)       

print(book1.book_info(),book1.book_borrowed())





