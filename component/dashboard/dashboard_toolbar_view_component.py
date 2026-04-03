from playwright.sync_api import Page, expect
from component.base_component import BaseComponent

class DashboardToolbarView(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id("dashboard-toolbar-title-text")

    def check_visible(self):
        expect(self.title).to_be_visible()