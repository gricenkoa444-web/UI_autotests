from playwright.sync_api import Page, expect
from element.base_element import BaseElement
import allure

class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "button"

    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Chacking that {self.type_of} "{self.name}" is enabled'):
            expect(locator).to_be_enabled()

    def check_disabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Checking that {self.type_of} "{self.name}" is disabled'):
            expect(locator).to_be_disabled()
