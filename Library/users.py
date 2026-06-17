class Users():

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def user_info(self):

        """Displays user information."""

        print(f"User ID: {self.user_id}\n"
              f"Name: {self.name}\n"
              f"Email: {self.email}\n")
        
        print(f"Borrowed books:")
        for books in self.borrowed_books:
            print(f"{books.title}")
                 
        
    def borrow_book(self, books):

        """Adds books to the user's list of borrowed books."""

        self.borrowed_books.append(books)

        print(f"{books.title} has been added to {self.name}'s borrowed books.")

    def return_book(self, books):

        """Removes books from the user's list of borrowed books."""

        if books in self.borrowed_books:
            self.borrowed_books.remove(books)
            print(f"{books.title} has been removed from {self.name}'s borrowed books.")
        else:
            print(f"{self.name} had not borrowed {books.title}.")

    def count_borrowed(self):

        """Counts the number of books borrowed by the user."""

        return len(self.borrowed_books)

user1 = Users(22, "Bob John", "bob.john@python.com")

print(user1.user_info())

    




