from component.courses.course_view_component import CourseViewComponent
from component.navigation.navbar_component import Navbar
from component.navigation.sidebar_component import SidebarComponent
from component.views.empty_view_component import EmptyViewComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = Navbar(page)
        self.empty_view = EmptyViewComponent(page, identifier="courses-list")
        self.course_view = CourseViewComponent(page)

        # title and create course button
        self.course_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")

    def check_visible_course_title(self):
        expect(self.course_title).to_be_visible()
        expect(self.course_title).to_have_text("Courses")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button_to_create(self):
        self.create_course_button.click()
