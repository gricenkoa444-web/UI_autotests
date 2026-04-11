import pytest
import allure
from pages.autorization.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.tags import AllureTag
from allure_commons.types import Severity

@pytest.mark.registration
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
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


