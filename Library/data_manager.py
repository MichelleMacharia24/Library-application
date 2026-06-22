import csv 
from books import Books
from users import Users
from borrowed import Borrowed

def save_books(books, filename="books.csv"):

    """Saves books into the csv file."""

    with open(filename,"w",newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["book_id","title","author","available"])

        for book in books:
            writer.writerow([
                book.book_id,
                book.title,
                book.author,
                book.available
            ])

def load_books(filename="books.csv"):

    """Loads books into library from csv."""

    books = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            book = Books(int(row[0]), row[1], row[2], row[3] == "True")
            books.append(book)

    return books 


def save_users(users, filename="users.csv"):

    """Saves users into CSV file."""

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["user_id", "name", "email"])

        for user in users:
            writer.writerow([
                user.user_id,
                user.name,
                user.email
            ])


def load_users(filename="users.csv"):

    """Loads users from CSV and recreates User objects."""

    users = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            user = Users(int(row[0]), row[1], row[2])
            users.append(user)

    return users


def save_records(records, filename="records.csv"):

    """Saves borrowing records into CSV."""

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["record_id", "user_id", "book_id", "borrow_date", "return_date"])

        for record in records:
            writer.writerow([
                record.record_id,
                record.user_id,
                record.book_id,
                record.borrow_date,
                record.return_date
            ])


def load_records(filename="records.csv"):
    """Loads borrowing records from CSV."""

    records = []

    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            record = Borrowed(int(row[0]), int(row[1]), int(row[2]))
            record.borrow_date = row[3] if row[3] != "None" else None
            record.return_date = row[4] if row[4] != "None" else None

            records.append(record)

    return records