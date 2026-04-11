from utils import books

def issue_books():
    book_name = input("Enter book name: ").strip().upper()
    if book_name in books and books[book_name] == "Available":
        books[book_name] = "Issued"
        print("Book issued successfully!")
    else:
        print("Book not available!")
