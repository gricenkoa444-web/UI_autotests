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

        # title and create course button
        self.course_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_button = page.get_by_test_id("courses-list-toolbar-create-course-button")
        # empty view
        #card's course
        self.course_title_1 = page.get_by_test_id("course-widget-title-text")
        self.course_image = page.get_by_test_id("course-preview-image")
        self.course_max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.course_min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.course_estimated_time = page.get_by_test_id("course-estimated-time-info-row-view-text")
        #menu's course
        self.course_menu_button = page.get_by_test_id("MoreVertIcon")
        self.course_edit_button = page.get_by_test_id("course-view-edit-menu-item-text")
        self.course_delete_button = page.get_by_test_id("course-view-delete-menu-item-text")

    def check_visible_course_title(self):
        expect(self.course_title).to_be_visible()
        expect(self.course_title).to_have_text("Courses")

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button_to_create(self):
        self.create_course_button.click()

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
    ):
        #this method "nth" - can help us to get locator with index.
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title_1.nth(index)).to_be_visible()
        expect(self.course_title_1.nth(index)).to_have_text(title)

        expect(self.course_max_score.nth(index)).to_be_visible()
        expect(self.course_max_score.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.course_min_score.nth(index)).to_be_visible()
        expect(self.course_min_score.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.course_estimated_time.nth(index)).to_be_visible()
        expect(self.course_estimated_time.nth(index)).to_have_text(f"Estimated time: {estimated_time}")


    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_button.nth(index)).to_be_visible()
        self.course_edit_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_button.nth(index)).to_be_visible()
        self.course_delete_button.nth(index).click()