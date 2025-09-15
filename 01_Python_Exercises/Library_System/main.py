from mylibrary import library

def show_menu():
    print("\nLibrary Menu:")
    print("1.Add")
    print("2.Remove")
    print("3.Search")
    print("4.Show Books")
    print("5.Exit")

if __name__ == "__main__":
    lib = library.Library()

    while True:
        show_menu()
        choice = int(input("Your Choice: "))
        
        if choice == 1:
            title = input("Title of your book you want to add: ")
            author = input("Author of your book: ")
            lib.add_book(title, author)
        elif choice == 2:
            title = input("Title of your book you want to remove: ")
            lib.remove_book(title)
            
        elif choice == 3:
            title = input("Title of your book you want to search: ")
            lib.search_book(title)
            
        elif choice == 4:
            print("There are your books:")
            lib.show_books()
            
        elif choice == 5:
            print("Have a good day!")
            break
        else:
            print("Choice is invalid")
