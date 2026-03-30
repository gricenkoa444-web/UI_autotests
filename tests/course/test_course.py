import pytest
from playwright.sync_api import Page, expect

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_courses(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    ...