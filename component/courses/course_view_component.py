from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from component.courses.courses_view_menu_component import CoursesViewMenuComponent
from element.image import Image
from element.text import Text


class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CoursesViewMenuComponent(page)

        self.course_title_1 = Text(page,"course-widget-title-text", "Course title")
        self.course_image = Image(page, "course-preview-image", "Image title")
        self.course_max_score = Text(page, "course-max-score-info-row-view-text", "Max score")
        self.course_min_score = Text(page, "course-min-score-info-row-view-text", "Min score")
        self.course_estimated_time = Text(page,"course-estimated-time-info-row-view-text", "Estimated")

    def check_visible_course_card(
            self,
            index: int,
            title: str,
            max_score: str,
            min_score: str,
            estimated_time: str,
    ):
        #this method "nth" - can help us to get locator with index.
        self.course_image.check_visible(nth=index)

        self.course_title_1.check_visible(nth=index)
        self.course_title_1.check_have_text(title, nth=index)

        self.course_max_score.check_visible(nth=index)
        self.course_max_score.check_have_text(f"Max score: {max_score}", nth=index)

        self.course_min_score.check_visible(nth=index)
        self.course_min_score.check_have_text(f"Min score: {min_score}", nth=index)

        self.course_estimated_time.check_visible(nth=index)
        self.course_estimated_time.check_have_text(f"Estimated time: {estimated_time}", nth=index)