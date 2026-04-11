from add_books import add_book
from show_books import show_book
from issue_books import issue_books
from return_books import return_books

def library():
    while True:
        print("\n==== LIBRARY MENU ====")
        print("\n1. Add Books")
        print("\n2. Show Books")
        print("\n3. Issue Books")
        print("\n4. Return Books")
        print("\n5. Exit")
        print("===========================")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)
        if choice==1: add_book()
        elif choice==2: show_book()
        elif choice==3: issue_books()
        elif choice==4: return_books()
        elif choice==5:
            print("Thank you.")
            break
        else:
            print("Invalid choice! Please try again.")
library()