import re
from pytest_playwright.pytest_playwright import page


class AddFavourites:
        def __init__(self, page):
            self.page = page

            self.book_name = page.get_by_test_id("fav-Playwright: Click It Till You Make It")




