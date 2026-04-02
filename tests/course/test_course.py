import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_courses(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.check_visible_create_course_title_1()
    create_course_page.check_visible_create_course_button_1()
    create_course_page.empty_view.check_visible(
        title='No image selected',
        description='Preview of selected image will be displayed here'
    )
    create_course_page.check_visible_image_upload_view_1()
    create_course_page.check_visible_create_course_form_1(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0",
    )
    create_course_page.check_visible_exercises_title_1()
    create_course_page.check_visible_create_exercise_button_1()
    create_course_page.check_visible_exercises_empty_view_1()
    create_course_page.upload_preview_image_1(file="./testdata/files/image.png")
    create_course_page.fill_create_course_form_1(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button_1()

    courses_list_page.check_visible_course_title()
    courses_list_page.check_visible_course_card(
         index=0,
         title="Playwright",
         max_score="100",
         min_score="10",
         estimated_time="2 weeks"
    )
    print(f"Test is passed! Course 'Playwright' is created!")
