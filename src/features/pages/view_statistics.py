import re

class Statistics:
    def __init__(self, page):
        self.page = page

        self.statistics_button = page.get_by_role("button", name="Statistik")
        self.welcome_heading = page.get_by_role("heading", name= " Välkommen! ")
        self.books_count = page.get_by_text(re.compile(r"Listan har \d+ böcker\."))
        self.favourites_count = page.get_by_text(re.compile(r"Våra användare har hjärtmarkerat \d+ böcker\."))