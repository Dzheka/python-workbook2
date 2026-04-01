class Book:
    def init(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def repr(self):
        return f"{self.title} by {self.author}"


class Library:
    def init(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(book)
