from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.text import Text


class DashboardToolbarView(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "dashboard-toolbar-title-text", "Title")

    def check_visible(self):
        self.title.check_visible()