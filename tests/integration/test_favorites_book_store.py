import pytest

from src.bookstore.book_store import BookStore
from src.bookstore.fav_books import FavoriteBooks

@pytest.mark.integration
def test_toggle_favorite_adds_book():
    # Arrange
    favorite = FavoriteBooks()
    store = BookStore(favorite)


    book = store.addBook("Python för folk som hatar ormar", "Monty Pythonsson")

    # Act
    store.toggleFavorite(book["id"])

    #Assert
    assert book in favorite.books

@pytest.mark.integration
def test_toggle_favorite_remove_book():
    # Arrange
    favorite = FavoriteBooks()
    store = BookStore(favorite)

    book = store.addBook("Python för folk som hatar ormar", "Monty Pythonsson")

    store.toggleFavorite(book["id"])

    # Act
    store.toggleFavorite(book["id"])

    # Assert
    assert book not in favorite.books