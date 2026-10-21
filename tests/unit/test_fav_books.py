from src.bookstore.fav_books import FavoriteBooks


def test_add():
    #Arrange
    fav_books = FavoriteBooks()

    #Act
    fav_books.add(123)

    #Assert
    assert fav_books.books[0] == 123






def test_remove():
    #Arrange
    fav_books = FavoriteBooks()
    fav_books.add(123)

    #Act
    fav_books.remove(123)

    #Assert
    assert fav_books.books[0] == 123