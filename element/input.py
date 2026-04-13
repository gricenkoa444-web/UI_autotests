from playwright.sync_api import Page, expect, Locator
from element.base_element import BaseElement
import allure

class Input(BaseElement):
    @property
    def type_of(self):
        return "input"

    def get_locator(self, nth: int = 0,  **kwargs) -> Locator:
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0,  **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Filling {self.type_of} "{self.name}" to value "{value}"'):
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} "{self.name}" to have value "{value}"'):
            expect(locator).to_have_value(value)

