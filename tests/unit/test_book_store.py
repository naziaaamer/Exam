from src.bookstore.book_store import BookStore


def test_add_book():
    #Arrange
    book_store = BookStore()

    #Act
    book_store.addBook("Python för folk som hatar ormar", "Monty Pythonsson")

    #Assert
    assert len(book_store.books) == 1
    assert book_store.books[0]["title"] == "Python för folk som hatar ormar"
    assert book_store.books[0]["author"] == "Monty Pythonsson"

