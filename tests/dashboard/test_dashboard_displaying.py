import pytest
from pages.dashboard.dashboard_page import DashboardPage
from tools.routes import AppRoute
from config import settings

@pytest.mark.regression
@pytest.mark.dashboard
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(AppRoute.DASHBOARD)
    dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
    dashboard_page_with_state.dashboard_toolbar.check_visible()
    dashboard_page_with_state.students_chart_view.check_visible(title="Students")
    dashboard_page_with_state.activities_chart_view.check_visible(title="Activities")
    dashboard_page_with_state.courses_chart_view.check_visible(title="Courses")
    dashboard_page_with_state.scores_chart_view.check_visible(title="Scores")
    dashboard_page_with_state.sidebar.check_visible()
    dashboard_page_with_state.sidebar.click_logout()

