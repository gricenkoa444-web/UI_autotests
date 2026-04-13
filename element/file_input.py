from playwright.sync_api import Page, expect
from element. base_element import BaseElement
import allure

class FileInput(BaseElement):
    @property
    def type_of(self):
        return 'file input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        with allure.step(f'Setting file "{file}" to the {self.type_of} "{self.name}"'):
            locator.set_input_files(file)

