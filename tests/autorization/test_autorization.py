from pages.autorization.login_page import LoginPage
import pytest

text="Wrong email or password"
@pytest.mark.login
@pytest.mark.regression
@pytest.mark.parametrize(
    "email, password", [
        ("user.name@gmail.com", "password"),
        ("username@gmail.com", " "),
    ]
)
def test_wrong_email_or_password_alert(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.login_form.fill(email=email, password=password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert(text=text)
