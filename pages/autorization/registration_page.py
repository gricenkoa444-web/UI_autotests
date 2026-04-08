from playwright.sync_api import Page, expect

from component.authentication.registration_form_component import RegistrationFormComponent
from element.button import Button
from element.link import Link
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.button = Button(page, "registration-page-registration-button", "Button")
        self.login_link = Link(page, "registration-page-login-link", "Login")

    def click_registration_button(self):
        self.button.click()

    def check_visible_login_link(self):
        self.login_link.check_visible()