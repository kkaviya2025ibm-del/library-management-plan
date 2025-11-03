class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies
    def __str__(self):
        return f"{self.title} by {self.author} (Available: {self.copies})"
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, copies=1):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += copies
                print(f"Added {copies} more copies of '{title}'.")
                return
        new_book = Book(title, author, copies)
        self.books.append(new_book)
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        print("\nAvailable Books:")
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.copies > 0:
                    book.copies -= 1
                    print(f"You have borrowed '{book.title}'. Please return it soon!")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.copies += 1
                print(f"Thank you for returning '{book.title}'.")
                return
        print(f"Book '{title}' does not belong to this library.")


def main():
    library = Library("City Library")

    while True:
        print("\n=== Library Management System ===")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            copies = int(input("Enter number of copies: "))
            library.add_book(title, author, copies)

        elif choice == "3":
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()