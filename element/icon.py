from element.base_element import BaseElement
import allure

class Icon(BaseElement):
    @property
    def type_of(self) -> str:
        return 'icon'