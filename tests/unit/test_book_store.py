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


def test_add_multiple_books():
    #Arrange
    book_store = BookStore()

    #Act
    book_store.addBook("The Developer Who Knew Nothing", "George R.R. Martin")
    book_store.addBook("Git Blame and Other Ways to Lose Friends", "Linus Torvalds")

    #Assert
    assert len(book_store.books) == 2
    assert book_store.books[0]["title"] == "The Developer Who Knew Nothing"
    assert book_store.books[0]["author"] == "George R.R. Martin"

    assert book_store.books[1]["title"] == "Git Blame and Other Ways to Lose Friends"
    assert book_store.books[1]["author"] == "Linus Torvalds"


def test_toggle_favorite():
    #Arrange
    book_store = BookStore()
    book_store.addBook("The Developer Who Knew Nothing", "George R.R. Martin")
    book_store.addBook("Git Blame and Other Ways to Lose Friends", "Linus Torvalds")

    #Act
    book_store.toggleFavorite(0)
    book_store.toggleFavorite(1)

    #Assert
    assert book_store.books[0]["favorite"] == True
    assert book_store.books[1]["favorite"] == True


