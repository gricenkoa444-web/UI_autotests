from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        self.page.goto(url, wait_until = "domcontentloaded")

    def reload(self):
        self.page.reload(wait_until = "networkidle")

