class BasePage():
    def __init__(self, page):
        self.page = page
        self.initial_heading = page.get_by_role("heading", name="Läslisten")
        self.welcome_heading = page.get_by_role("heading", name=" Välkommen!")


    def navigate_to_web(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/", timeout=15000)