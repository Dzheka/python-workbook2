class Book():
    def __init__(self,title,author, isbn) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self) -> str:
        return f"{self.title} by {self.author}"



class Library():
    def __init__(self,name,books = []) -> None:
        self.name = name
        self.books = books

    def add_book(self, n_book):
        self.books.append(n_book)
        print(f"Added: {n_book}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def list_books(self):
        for book in self.books:
            print(f"{Book(book.title, book.author, book.isbn)}")

library = Library("City Library")
book1 = Book("1984", "George Orwell", "123")
book2 = Book("Dune", "Frank Herbert", "456")

library.add_book(book1)
library.add_book(book2)

found = library.find_book("1984")
print(found)  # 1984 by George Orwell

library.list_books()
