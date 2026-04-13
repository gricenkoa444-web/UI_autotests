from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.input import Input
import allure

class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Email Input Registration")
        self.username_input = Input(page, "registration-form-username-input", "Username Registration" )
        self.password_input = Input(page, "registration-form-password-input", "Password Registration")

    @allure.step('Fill registration form')
    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step('Check visible registration form')
    def check_visible(self):
        self.email_input.check_visible()

        self.username_input.check_visible()

        self.password_input.check_visible()