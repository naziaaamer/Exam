

class FavoriteBooks:
    def __init__(self):
        self.books = []


    def add(self,book_id):
        self.books.append(book_id)


    def remove(self,book_id):
        self.books.remove(book_id)