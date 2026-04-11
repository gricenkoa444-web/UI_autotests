import pytest
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
import allure

@pytest.mark.regression
@pytest.mark.dashboard
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
def test_dashboard_page_visible(dashboard_page: DashboardPage):
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page.dashboard_toolbar.check_visible()
    dashboard_page.students_chart_view.check_visible(title="Students")
    dashboard_page.activities_chart_view.check_visible(title="Activities")
    dashboard_page.courses_chart_view.check_visible(title="Courses")
    dashboard_page.scores_chart_view.check_visible(title="Scores")
