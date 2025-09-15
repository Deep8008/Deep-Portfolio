class Library():
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})
        print(f"You succsessfuly added ({title}) book wrote by ({author})")
    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"You succsessfuly removed ({title})")
            else:
                print(f"Removing was unsuccessful, ({title}) book not found")
    def search_book(self, title):
        for book in self.books:
            if not book["title"] == title:
                print(f"({title}) not found")
                
            else:
                print(f"({book['title']}) book wrote by ({book['author']}) Found!")

    def show_books(self):
        if not self.books:
            print("There is no book here")
        else:
            for index, book in enumerate(self.books, 1):
                print(f"{index}. {book['title']} - {book['author']}")
