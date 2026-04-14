import pytest
import allure
from pages.autorization.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.stories import AllureStory
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from config import settings

from tools.routes import AppRoute


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
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.check_visible_login_link()
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()


