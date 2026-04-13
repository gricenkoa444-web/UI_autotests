from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.input import Input
import allure


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "login-form-email-input", "Email Input")
        self.password_input = Input(page, "login-form-password-input", "Password Input")

    @allure.step('Fill login form')
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    @allure.step('Check visible login form')
    def check_visible(self):
        self.email_input.check_visible()

        self.password_input.check_visible()