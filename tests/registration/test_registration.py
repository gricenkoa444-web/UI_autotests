from playwright.sync_api import Page, expect
import pytest

from pages.registration_page import RegistrationPage

@pytest.mark.registration
@pytest.mark.regression
@pytest.mark.parametrize("email,username,password", [
    ("user.name@gmail.com", "test_username", "password"),
])
def test_successful_registration(
        registration_page: RegistrationPage,
        email: str,
        username: str,
        password: str
):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.check_visible_login_link()
    registration_page.fill_registration_form(email=email, username=username, password=password)
    registration_page.click_registration_button()

