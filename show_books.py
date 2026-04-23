from utils import books

def show_book():
    if not books:
        print("No books available")
    else:
        print("\nAvailable Books:")
        for book, info in books.items():
            print(f"{book} -> {info['status']}")