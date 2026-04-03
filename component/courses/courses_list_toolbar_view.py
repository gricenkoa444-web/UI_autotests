from playwright.sync_api import Page, expect
from component.base_component import BaseComponent

class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")

    def check_visible_course_title(self):
        expect(self.course_title).to_be_visible()
        expect(self.course_title).to_have_text("Courses")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button_to_create(self):
        self.create_course_button.click()