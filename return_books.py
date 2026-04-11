from utils import books

def return_books():
        book_name = input("Enter book name to return: ").strip().upper()

        if book_name in books and books[book_name] == "Issued":
            books[book_name] = "Available"
            print("Book returned successfully!")
        else:
            print("Book was not taken.")