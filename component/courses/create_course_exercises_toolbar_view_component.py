from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.button import Button
from element.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-exercises-box-toolbar-title-text", "Title")
        self.button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", "Button to create exercise"
        )

    def check_disabled_button(self):
        self.button.check_disabled()

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

    def check_visible_button(self):
        self.button.check_visible()

    def click_button(self):
        self.button.click()