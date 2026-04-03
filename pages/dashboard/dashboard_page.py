from playwright.sync_api import Page, expect

from component.charts.chart_view_component import ChartViewComponent
from component.dashboard.dashboard_toolbar_view_component import DashboardToolbarView
from component.navigation.navbar_component import Navbar
from component.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarView(page)
        self.navbar = Navbar(page)
        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

