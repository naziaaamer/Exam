import re

from pytest_playwright.pytest_playwright import page


class AddFavourites:
        def __init__(self, page):
            self.page = page
            self.hover_favourites = page.get_by_test_id("star-Playwright: Click It Till You Make It")
            self.favourites_button = page.get_by_text(re.compile("star-Python för folk som hatar ormar"))
            self.favourites_button_visible = page.get_by_test_id("star-Playwright: Click It Till You Make It")
            self.mina_bocker_button = page.get_by_role("button", name="Mina böcker")
            self.book_name = page.get_by_test_id("fav-Python för folk som hatar ormar")



        def navigate(self):
            self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/", timeout=15000)



