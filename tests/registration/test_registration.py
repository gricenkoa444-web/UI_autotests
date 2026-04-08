import pytest
import allure
from pages.autorization.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.mark.registration
@pytest.mark.regression
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    def test_successful_registration_correct(
            self,
            registration_page: RegistrationPage,
            dashboard_page: DashboardPage,
    ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.check_visible_login_link()
        registration_page.registration_form.fill(
            email="user.name@gmail.com", username="test_username", password="password"
        )
        registration_page.click_registration_button()


