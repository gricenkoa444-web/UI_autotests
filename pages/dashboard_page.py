from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id("dashboard-toolbar-title-text")
        self.student_text = page.get_by_test_id("students-widget-title-text")
        self.active_text = page.get_by_test_id("activities-widget-title-text")
        self.courses_text = page.get_by_test_id("courses-widget-title-text")
        self.scores_text = page.get_by_test_id("scores-widget-title-text")

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.student_text).to_be_visible()
        expect(self.active_text).to_be_visible()
        expect(self.courses_text).to_be_visible()
        expect(self.scores_text).to_be_visible()