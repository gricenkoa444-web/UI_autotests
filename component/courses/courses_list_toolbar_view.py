from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.button import Button
from element.text import Text


class CoursesListToolbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title = Text(page, "courses-list-toolbar-title-text", "Course list title")
        self.create_course_button = Button(
            page, "courses-list-toolbar-create-course-button", "Button to create course"
        )

    def check_visible_course_title(self):
        self.course_title.check_visible()
        self.course_title.check_have_text("Courses")

    def check_visible_create_course_button(self):
        self.create_course_button.check_visible()

    def click_create_course_button_to_create(self):
        self.create_course_button.click()