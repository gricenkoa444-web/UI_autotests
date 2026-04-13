from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.button import Button
from element.text import Text
import allure

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-exercises-box-toolbar-title-text", "Title")
        self.button = Button(
            page, "create-course-exercises-box-toolbar-create-exercise-button", "Button to create exercise"
        )

    def check_disabled_button(self):
        self.button.check_disabled()

    @allure.step('Check visible title and that it has text "Exercises"')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

    @allure.step('Check visible create course button')
    def check_visible_button(self):
        self.button.check_visible()

    def click_button(self):
        self.button.click()