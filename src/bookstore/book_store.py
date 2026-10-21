class BookStore:
    def __init__(self):
        self.books = []

    def addBook(self, title, author):
        books = {
            "title": title,
            "author": author
        }
        self.books.append(books)

    def toggleFavorite(self, book_id):
        pass