import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_courses(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.create_course_toolbar_view.check_visible_button()
    create_course_page.image_upload_widget.check_visible()
    create_course_page.create_course_form.check_visible(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0",
    )
    create_course_page.create_course_exercises_toolbar.check_visible()
    create_course_page.create_course_exercises_toolbar.check_visible_button()
    create_course_page.check_visible_exercises_empty_view_1()
    create_course_page.image_upload_widget.upload_image(file="./testdata/files/image.png")
    create_course_page.create_course_form.fill(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.create_course_toolbar_view.click()

    courses_list_page.course_list_toolbar.check_visible_course_title()
    courses_list_page.course_view.check_visible_course_card(
         index=0,
         title="Playwright",
         max_score="100",
         min_score="10",
         estimated_time="2 weeks"
    )
    print(f"Test is passed! Course 'Playwright' is created!")
