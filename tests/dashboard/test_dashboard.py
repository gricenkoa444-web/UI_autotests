from playwright.sync_api import Page, expect
import pytest
from pages.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_page_visible(dashboard_page: DashboardPage):
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page.check_visible_dashboard_title()
    dashboard_page.check_visible_students_chart()
    dashboard_page.check_visible_activities_chart()
    dashboard_page.check_visible_courses_chart()
    dashboard_page.check_visible_scores_chart()
