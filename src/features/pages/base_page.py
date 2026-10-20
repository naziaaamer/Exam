from asyncio import timeout


class BasePage():
    def __init__(self, page):
        self.page = page
        self.initial_heading = page.get_by_role("heading", name=" Läslistan ")
        self.welcome_heading = page.get_by_role("heading", name=" Välkommen!")
        self.favourites_button = page.get_by_test_id("star-Playwright: Click It Till You Make It")
        self.favourites_icon = page.locator("div.star.selected")
        self.mina_booker_button = page.get_by_role("button", name="Mina böcker")


    def navigate_to_web(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/", timeout=5000)