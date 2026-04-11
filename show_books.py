from utils import books

def show_book():
    if not books: 
        print("No book available")
    else:
        print("Available Books:")
        for book,status in books.item():
            print(f"{books} > {status}")