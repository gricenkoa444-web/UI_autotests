from element.base_element import BaseElement
import allure

class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return 'link'
