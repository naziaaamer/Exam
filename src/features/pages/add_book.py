import re


class AddBook:
    def __init__(self,page):
        self.page = page
        self.book_title = self.page.get_by_text(re.compile("if tomorrow comes"))
        self.add_book_button = self.page.get_by_role("button", name="Lägg till bok")
        self.book_name = self.page.get_by_role("textbox", name="Titel")
        self.author_name = self.page.get_by_role("textbox", name="Författare")
        self.add_new_book = self.page.get_by_role("button", name="Lägg till ny bok")
        self.katalog_button = self.page.get_by_role("button", name="Katalog")

    def navigate(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/", timeout=15000)







