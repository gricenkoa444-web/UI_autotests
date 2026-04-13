from element.base_element import BaseElement
import allure

class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return 'text'
