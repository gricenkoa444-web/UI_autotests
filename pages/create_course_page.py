from component.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from component.views.empty_view_component import EmptyViewComponent
from component.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, identifier="create-course-preview")
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier="create-course-preview")
        self.create_course_exercises_form = CreateCourseExerciseFormComponent(page)
        #title and create course button
        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_button_1 = page.get_by_test_id("create-course-toolbar-create-course-button")
        #form create course
        self.create_course_title_input = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.create_course_estimated_time_input = page.get_by_test_id(
            "create-course-form-estimated-time-input"
        ).locator("input")
        self.create_course_description_textarea =(
            page.get_by_test_id(
            "create-course-form-description-input"
        ).locator("textarea").first
        )
        self.create_course_max_score_input = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.create_course_min_score_input = page.get_by_test_id("create-course-form-min-score-input").locator("input")

        #toolbar exercises
        self.exercises_title = page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.create_course_button = page.get_by_test_id(
            "create-course-exercises-box-toolbar-create-exercise-button"
        )
        #block exercises
        self.exercises_empty_view_icon = page.get_by_test_id("create-course-exercises-empty-view-icon")
        self.exercises_empty_title_text = page.get_by_test_id("create-course-exercises-empty-view-title-text")
        self.exercises_empty_description_text = page.get_by_test_id(
            "create-course-exercises-empty-view-description-text"
        )

    def check_visible_create_course_title_1(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')

    def click_create_course_button_1(self):
        self.create_course_button_1.click()

    def check_visible_create_course_button_1(self):
        expect(self.create_course_button_1).to_be_visible()

    def check_disabled_create_course_button_1(self):
        expect(self.create_course_button).to_be_disabled()

    def check_visible_create_course_form_1(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        expect(self.create_course_title_input).to_be_visible()
        expect(self.create_course_title_input).to_have_value(title)

        expect(self.create_course_estimated_time_input).to_be_visible()
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        expect(self.create_course_description_textarea).to_be_visible()
        expect(self.create_course_description_textarea).to_have_value(description)

        expect(self.create_course_max_score_input).to_be_visible()
        expect(self.create_course_max_score_input).to_have_value(max_score)

        expect(self.create_course_min_score_input).to_be_visible()
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def fill_create_course_form_1(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_title_input.fill(title)
        expect(self.create_course_title_input).to_have_value(title)

        self.create_course_estimated_time_input.fill(estimated_time)
        expect(self.create_course_estimated_time_input).to_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        expect(self.create_course_description_textarea).to_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        expect(self.create_course_max_score_input).to_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        expect(self.create_course_min_score_input).to_have_value(min_score)

    def check_visible_exercises_title_1(self):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Exercises')

    def check_visible_create_exercise_button_1(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_exercise_button_1(self):
        self.create_course_button.click()

    def check_visible_exercises_empty_view_1(self):
        expect(self.exercises_empty_view_icon).to_be_visible()

        expect(self.exercises_empty_title_text).to_be_visible()
        expect(self.exercises_empty_title_text).to_have_text('There is no exercises')

        expect(self.exercises_empty_description_text).to_be_visible()
        expect(self.exercises_empty_description_text).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )





