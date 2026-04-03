from playwright.sync_api import Page, expect

from component.authentication.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)\

        self.registration_form = RegistrationFormComponent(page)

        self.button = page.get_by_test_id("registration-page-registration-button")
        self.login_link = page.get_by_test_id("registration-page-login-link")

    def click_registration_button(self):
        self.button.click()

    def check_visible_login_link(self):
        expect(self.login_link).to_be_visible()