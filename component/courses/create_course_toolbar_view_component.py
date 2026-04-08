from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.button import Button
from element.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-toolbar-title-text", "Title")
        self.button = Button(page, "create-course-toolbar-create-course-button", "Button to create course")

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

    def click(self):
        self.button.click()

    def check_visible_button(self, is_create_course_disabled=True):
        self.button.check_visible()

        if is_create_course_disabled:
            self.button.check_disabled()
        else:
            self.button.check_enabled()

