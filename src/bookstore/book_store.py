class BookStore:
    def __init__(self, favorite_books=None):
        self.books = []
        self.next_book_id = 1
        self.favorite_books = favorite_books
        self.favorite_ids = set()

    def addBook(self, title, author):
        book = {
            "id": self.next_book_id,
            "title": title,
            "author": author,
        }

        self.books.append(book)
        self.next_book_id += 1

        return book


    def toggleFavorite(self, book_id):
        book = next(
            (b for b in self.books if b["id"] == book_id), None
        )

        if book is None:
            raise ValueError("Book not found")

        if book_id in self.favorite_ids:
            self.favorite_ids.remove(book_id)
            self.favorite_books.remove(book)
        else:
            self.favorite_ids.add(book_id)
            self.favorite_books.add(book)
