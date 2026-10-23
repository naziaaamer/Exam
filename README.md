# Python with Playwright Exam
 
## Project Overview:
The purpose is to test the functionality of The Reading List web application using automated tests for both the backend and frontend.

Website: https://tap-vt26-testautomatisering.github.io/exam/

## What Is Tested?
- Backend

    The backend is implemented in Python and contains two classes:

        BookStore — adds books and toggles their favorite status.
        FavoriteBooks — adds and removes books from the favorites collection.

    The backend tests include:

        Unit tests for all four required methods.
        Integration tests verifying that the classes work together.

- Frontend

    The frontend is tested using Playwright and BDD-style feature files using POM style.

        The tests cover:

            Catalog: Browsing books and marking or unmarking favorites.
            Add Book: Adding new books and checking form behavior.
            My Books: Viewing favorite books and removing favorites.
            Statistics: Testing the statistics view.

## Technologies 
    Python
    pytest
    Playwright
    pytest-bdd
    Git and GitHub
    GitHub Actions

## Prerequisites

    Python installed.
    Git installed.
    The dependencies listed in requirements.txt.
    Playwright and its required browser installed.

## Run Tests
    Frontend:
                    python -m behave src/features in terminal
        
    Backend:
        All tests:  
                    pytest
        Unit: 
                    pytest -m unit -v
        Integration:
                    pytest -m integration -v
    
## Continuous Integration

    GitHub Actions is used to run automated tests when code is pushed to the main branch.
        The workflow is located at:
            .github/workflows/python-ci.yml
        The workflow installs the required dependencies and browser, then runs the tests in headless mode.

## Project structure

Exam/
├ .GitHub/
| ├─ workflows/
| | ├─ python-ci.yml/
├─ src/
| ├─ bookstore/
| | └─ book_store.py
| | └─ fav_books.py
| ├─ features/
| | ├─ pages/
| | | └─ add_book.py
| | | └─ add_to_favorites.py
| | | └─ base_page.py
| | | └─ view_statistics.py
| | ├─ steps/
| | | └─ step_add_book.py
| | | └─ step_add_to_favourites.py
| | | └─ step_remove_favourites.py
| | | └─ step_view_catalog.py
| | | └─ step_view_statistics.py
| | ├─ feature_files.feature
| | └─ environment.py
├─ tests/
| ├─ unit/
| | └─ test_book_store.py
| | └─ test_fav_books.py
| └─ integration/
|   └─ test_favorites_book_store.py
├─ .gitignore
├─ ANSWERS.md
├─ behave.ini
├─ pytest.ini
├─ README.md
└─ requirements.txt
├─ STORIES.md