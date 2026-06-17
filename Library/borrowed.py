class Borrowed():

    def __init__(self, record_id, user_id, book_id):
        self.record_id = record_id
        self.user_id = user_id
        self.book_id = book_id
        self.borrow_date = None
        self.return_date = None

    def record_info(self):

        """Displays the record information."""

        print(f"Record ID: {self.record_id}\n"
              f"User ID: {self.user_id}\n"
              f"Book ID: {self.book_id}\n"
              f"Borrowed on: {self.borrow_date}\n"
              f"Returned on: {self.return_date}")
        
    def new_record(self, borrow_date):

        """Creates a new record using the borrow date."""

        self.borrow_date = borrow_date

    def close_record(self, return_date):

        """Closes an open record using the return date."""

        self.return_date = return_date

    def check_returned(self, return_date):

        """Checks if a book has been returned."""

        if self.return_date is None:
            return False
        else:
            return True