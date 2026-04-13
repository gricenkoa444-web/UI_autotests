from playwright.sync_api import Page
from component.base_component import BaseComponent
from component.navigation.sidebar_list_item import SidebarListItemComponent
import re
import allure

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page, "logout")
        self.courses_list_item = SidebarListItemComponent(page, "courses")
        self.dashboard_list_item = SidebarListItemComponent(page, "dashboard")

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.logout_list_item.check_visible('Logout')
        self.courses_list_item.check_visible('Courses')
        self.dashboard_list_item.check_visible('Dashboard')

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"))

    @allure.step('Click courses on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"))

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"))