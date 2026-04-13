from component.courses.course_view_component import CourseViewComponent
from component.courses.courses_list_toolbar_view import CoursesListToolbarComponent
from component.navigation.navbar_component import Navbar
from component.navigation.sidebar_component import SidebarComponent
from component.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect
import allure

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = Navbar(page)
        self.empty_view = EmptyViewComponent(page, identifier="courses-list")
        self.course_view = CourseViewComponent(page)
        self.course_list_toolbar = CoursesListToolbarComponent(page)
