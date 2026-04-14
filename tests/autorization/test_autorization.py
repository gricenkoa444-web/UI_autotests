from fixtures.page import dashboard_page
from pages.autorization.login_page import LoginPage
import pytest
import allure
from tools.allure.features import AllureFeature
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from pages.autorization.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from allure_commons.types import Severity

from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @pytest.mark.parametrize(
        "email, password", [
            ("user.name@gmail.com", "password"),
            ("username@gmail.com", " "),
        ]
    )
    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("User login with wrong email or password")
    @allure.severity(Severity.CRITICAL)
    def test_wrong_email_or_password_alert(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert(text="Wrong email or password")

    @allure.tag(AllureTag.USER_LOGIN)
    @allure.title("Navigation form login to registration")
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage,
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form.fill(email="test@gmail.com", password="password")
        login_page.click_login_button()
        login_page.click_registration_link()
        registration_page.registration_form.check_visible()
        registration_page.check_visible_login_link()
        registration_page.registration_form.fill(email="test@gmail.com", username="test_username", password="password")
        registration_page.click_registration_button()



