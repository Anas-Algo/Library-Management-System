from utils import books

def add_book():
    book_name = input("Enter book name to add: ").strip().upper()
    if book_name in books:
        print("Book already exists!")
    else:
        books[book_name] = "Available"
        print(f"Book - {book_name} added successfuly.")