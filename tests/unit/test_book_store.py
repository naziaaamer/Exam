from src.bookstore.book_store import BookStore
from src.bookstore.fav_books import FavoriteBooks


def test_add_book():
    #Arrange
    book_store = BookStore()

    #Act
    book = book_store.addBook("Python för folk som hatar ormar", "Monty Pythonsson")

    #Assert
    assert len(book_store.books) == 1
    assert book["title"] == "Python för folk som hatar ormar"
    assert book["author"] == "Monty Pythonsson"
    assert book["id"] == 1


def test_toggle_favorite_adds_book__mock(mocker):
    mock_favorites = mocker.Mock(spec=FavoriteBooks)
    store = BookStore(mock_favorites)

    book = store.addBook("Python for beginners", "Alex")

    store.toggleFavorite(book["id"])

    mock_favorites.add.assert_called_once_with(book)
    mock_favorites.remove.assert_not_called()


def test_toggle_favorite_removes_book__mock(mocker):
    mock_favorites = mocker.Mock(spec=FavoriteBooks)
    store = BookStore(mock_favorites)

    book = store.addBook("Python for beginners", "Alex")

    store.toggleFavorite(book["id"])
    mock_favorites.reset_mock()

    store.toggleFavorite(book["id"])

    mock_favorites.remove.assert_called_once_with(book)
    mock_favorites.add.assert_not_called()

