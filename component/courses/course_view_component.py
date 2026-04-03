from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.courses.courses_view_menu_component import CoursesViewMenuComponent

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CoursesViewMenuComponent(page)

        self.course_title_1 = page.get_by_test_id("course-widget-title-text")
        self.course_image = page.get_by_test_id("course-preview-image")
        self.course_max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.course_min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.course_estimated_time = page.get_by_test_id("course-estimated-time-info-row-view-text")

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