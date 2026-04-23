from utils import books

def issue_books():
    book_name = input("Enter book name: ").strip().upper()

    if book_name in books and books[book_name]["status"] == "Available":
        student = input("Enter student name: ")
        days = int(input("Enter number of days: "))

        books[book_name]["status"] = "Issued"
        books[book_name]["student"] = student
        books[book_name]["days"] = days

        print("Book issued successfully!")
    else:
        print("Book not available!")