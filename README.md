# Library Application
# Done by: Michelle Wangechi Macharia
## Final individual project for B100A Python Programming course.

## Purpose
The purpose of this application is to allow users to borrow and return books 
from this library system. The system also allows books to be added, removed and 
searched for. There is an included user menu interface that allows users to 
interact with the library system to pick their service of choice.

## Installation and execution
To install this program:
1. Have a python IDE.
2. Download or copy the files into one folder.
3. Open the terminal of the folder
4. Run 'python main.py'
5. Follow the steps in the interface.

## Example usage
To borrow a book:
Select option 3 and enter a valid book ID. The book's availability will be updated.

To return a book:
Select option 4 and enter a valid book ID. The book will become available again.

## Key features
- View all the library books
- Add new books to library
- Borrow library books
- Return library books
- Save or load data from csv files
- Use menu-driven user interface

## Key files
### Main.py
Holds the menu-driven user interface.

### Books.py
Contains the Books class.

### Users.py
Contains the Users class.

### Borrowed.py
Contains the Borrowed class.

### Library.py
Contains the Library class.

### Data_manager.py
Holds the functions that control the system.

### Test.py
Contains basic tests on the library system.

### Books.csv
Holds book items.

### Users.csv
Holds user information.

### Records.csv
Holds library records.