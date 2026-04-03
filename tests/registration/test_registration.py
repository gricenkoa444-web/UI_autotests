import pytest

from pages.autorization.registration_page import RegistrationPage

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
    registration_page.registration_form.fill(email=email, username=username, password=password)
    registration_page.click_registration_button()

