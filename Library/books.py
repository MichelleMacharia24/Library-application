class Books():

    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def book_info(self):

        """Displays the information about the book."""

        print(f"Book ID: {self.book_id}\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Availability: {self.available}")
        

    def borrow_book(self):

        """Marks a book as borrowed."""

        if self.available == True:
            self.available = False
            print(f"{self.title} has been succesffully borrowed.")
        else:
            print(f"{self.title} is already borrowed.")

    def return_book(self):

        """Marks a book as returned."""

        if self.available == False:
            self.available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} has not been returned.")

    def update_book(self, new_title, new_author):

        """Updates the details of an exisiting book."""

        self.title = new_title
        self.author = new_author

        print("Book details updated.")