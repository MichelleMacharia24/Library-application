class Books():

    def __init__(self, book_id, title, author, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def book_info(self):

        """
        Displays the information about the book.
        """

        print(f"Book ID: {self.book_id}\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Availability: {self.available}")