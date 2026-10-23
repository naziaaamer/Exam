import pytest
from src.bookstore.fav_books import FavoriteBooks


@pytest.fixture
def fav_books():
    return FavoriteBooks()


def test_add(fav_books):
    book = {
        "id": 1,
        "title": "if tomorrow comes",
        "author": "Sidney Sheldon",
    }

    #Act
    fav_books.add(book)

    #Assert
    assert fav_books.books[0] == book


def test_remove(fav_books):
    book = {
        "id": 1,
        "title": "if tomorrow comes",
        "author": "Sidney Sheldon",
    }

    fav_books.add(book)

    #Act
    fav_books.remove(book)

    #Assert
    assert book not in fav_books.books