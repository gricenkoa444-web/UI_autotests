from component.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from component.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from component.courses.create_course_form_component import CreateCourseFormComponent
from component.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from component.views.empty_view_component import EmptyViewComponent
from component.views.image_upload_widget_component import ImageUploadWidgetComponent
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_toolbar_view = CreateCourseToolbarViewComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier="create-course-preview")
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier="create-course-preview")
        self.create_course_exercises_form = CreateCourseExerciseFormComponent(page)

        #block exercises
        self.exercises_empty_view_icon = page.get_by_test_id("create-course-exercises-empty-view-icon")
        self.exercises_empty_title_text = page.get_by_test_id("create-course-exercises-empty-view-title-text")
        self.exercises_empty_description_text = page.get_by_test_id(
            "create-course-exercises-empty-view-description-text"
        )

    def check_visible_exercises_empty_view_1(self):
        expect(self.exercises_empty_view_icon).to_be_visible()

        expect(self.exercises_empty_title_text).to_be_visible()
        expect(self.exercises_empty_title_text).to_have_text('There is no exercises')

        expect(self.exercises_empty_description_text).to_be_visible()
        expect(self.exercises_empty_description_text).to_have_text(
            'Click on "Create exercise" button to create new exercise'
        )





