from book import Book
from dvd import DVD


def main():
    book1 = Book("The Hobbit", "B101", "J.R.R. Tolkien")
    dvd1 = DVD("Inception", "D202", 148)

    print("Book Information:")
    print(book1)
    print()

    print("DVD Information:")
    print(dvd1)
    print()

    if (book1.check_out()):
        print(f"{book1.title} has been checked out.")
    else:
        print(f"{book1.title} is already checked out.")

    if (book1.return_item()):
        print(f"{book1.title} has been returned.")
    else:
        print(f"{book1.title} was not checked out.")
    
    print()

    if (dvd1.check_out()):
        print(f"{dvd1.title} has been checked out.")
    else:
        print(f"{dvd1.title} is already checked out.")
    
    print()
    print("Updated DVD Information:")
    print(dvd1)

if __name__ == "__main__":
    main()