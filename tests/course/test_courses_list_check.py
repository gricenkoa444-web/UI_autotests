from playwright.sync_api import Page, expect
import pytest
from pages.courses_list_page import CoursesListPage

@pytest.mark.regression
def test_course_list_empty_view(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible(f' test_username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.check_visible_course_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.empty_view.check_visible(
        title='There is no results',
        description='Results from the load test pipeline will be displayed here'
    )
