import pytest
from pages.dashboard.dashboard_page import DashboardPage

@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_page_visible(dashboard_page: DashboardPage):
    dashboard_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    dashboard_page.dashboard_toolbar.check_visible()
    dashboard_page.students_chart_view.check_visible(title="Students")
    dashboard_page.activities_chart_view.check_visible(title="Activities")
    dashboard_page.courses_chart_view.check_visible(title="Courses")
    dashboard_page.scores_chart_view.check_visible(title="Scores")
