from playwright.sync_api import Page, expect

from component.authentication.login_form_component import LoginFormComponent
from element.button import Button
from element.link import Link
from element.text import Text
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, "login-page-login-button", "Login")
        self.wrong_alert = Text(
            page, "login-page-wrong-email-or-password-alert", "Wrong email or password"
                                )
        self.registration_link = Link(page, "login-page-registration-link", "Registration")

    def check_visible_wrong_email_or_password_alert(self, text: str):
        self.wrong_alert.check_visible()
        self.wrong_alert.check_have_text(text)

    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()



