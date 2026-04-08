from playwright.sync_api import Page, expect

from component.base_component import BaseComponent
from element.text import Text


class Navbar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.app_title = Text(page, "navigation-navbar-app-title-text", "App title")
        self.welcome_title = Text(page, "navigation-navbar-welcome-title-text", "Welcome title")

    def check_visible(self, username: str):
        self.app_title.check_visible()
        self.app_title.check_have_text('UI Course')

        self.welcome_title.check_visible()
        self.welcome_title.check_have_text(f"Welcome, {username}!")




