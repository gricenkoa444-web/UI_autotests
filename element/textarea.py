from playwright.sync_api import Locator, expect
import allure
from element.base_element import BaseElement


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def get_locator(self, nth: int = 0,  **kwargs) -> Locator:
        # Получаем локатор textarea
        return super().get_locator(nth, **kwargs).locator('textarea').first

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Filling {self.type_of} "{self.name}" to value "{value}"'):
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking {self.type_of} "{self.name}" to have value "{value}"'):
            expect(locator).to_have_value(value)