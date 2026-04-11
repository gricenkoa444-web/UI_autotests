from enum import Enum

class AllureTag(str, Enum):
    REGRESSION = "Regression"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"
    SMOKE = "Smoke"
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    USER_LOGIN = "User login"