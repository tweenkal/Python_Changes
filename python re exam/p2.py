class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # True if available, False if checked out

    def display_info(self):
        """Display book information."""
        status = "Available" if self.available else "Checked out"
        print(
            f'Title: "{self.title}", Author: {self.author}, Status: {status}')


class Library:
    """Represents the library system."""

    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        """Add a new book."""
        self.books.append(Book(title, author))
        print(f'Book "{title}" by {author} added.')

    def check_out_book(self, title):
        """Check out a book if available."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f'You have checked out "{book.title}".')
                else:
                    print(f'"{book.title}" is already checked out.')
                return
        print(f'Book "{title}" not found.')

    def return_book(self, title):
        """Return a book to make it available."""
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f'You have returned "{book.title}".')
                else:
                    print(f'"{book.title}" was not checked out.')
                return
        print(f'Book "{title}" not found.')

    def search_books(self, keyword):
        """Search books by title or author."""
        results = [book for book in self.books if
                   keyword.lower() in book.title.lower()
                   or keyword.lower() in book.author.lower()]
        if results:
            print(f'Books matching "{keyword}":')
            for book in results:
                book.display_info()
        else:
            print(f'No books found for "{keyword}".')

    def list_available_books(self):
        """List all available books."""
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books:")
            for book in available_books:
                book.display_info()
        else:
            print("No books are currently available.")

    def display_book_info(self, title):
        """Display information about a specific book."""
        for book in self.books:
            if book.title.lower() == title.lower():
                book.display_info()
                return
        print(f'Book "{title}" not found.')


# Instantiate the Library
library = Library()

# Menu-driven interaction
while True:
    print("\n--- Library Management System ---")
    print("1. Add a new book")
    print("2. Check out a book")
    print("3. Return a book")
    print("4. Search for books")
    print("5. List available books")
    print("6. Display book information")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(title, author)

    elif choice == "2":
        title = input("Enter book title to check out: ")
        library.check_out_book(title)

    elif choice == "3":
        title = input("Enter book title to return: ")
        library.return_book(title)

    elif choice == "4":
        keyword = input("Enter title or author to search: ")
        library.search_books(keyword)

    elif choice == "5":
        library.list_available_books()

    elif choice == "6":
        title = input("Enter book title to display info: ")
        library.display_book_info(title)

    elif choice == "7":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
