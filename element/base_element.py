from playwright.sync_api import Page, expect, Locator
import allure

class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        with allure.step(f'Getting locator with "data_testid={locator}" at index "{nth}"'):
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Clicking on {self.type_of} "{self.name}"'):
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking visibility of {self.type_of} "{self.name}" is visible'):
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} "{self.name}" has text "{text}"'):
            expect(locator).to_have_text(text)

        


