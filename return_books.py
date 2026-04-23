from utils import books

def return_books():
    book_name = input("Enter book name to return: ").strip().upper()

    if book_name in books and books[book_name]["status"] == "Issued":
        actual_days = int(input("Enter how many days you kept the book: "))
        allowed_days = books[book_name]["days"]

        if actual_days > allowed_days:
            late_days = actual_days - allowed_days
            fine = late_days * 10
            print(f"Late return! Fine = ₹{fine}")
        else:
            print("Book returned on time. No fine.")

        # reset book
        books[book_name]["status"] = "Available"
        books[book_name]["student"] = ""
        books[book_name]["days"] = 0

        print("Book returned successfully!")
    else:
        print("Invalid return!")