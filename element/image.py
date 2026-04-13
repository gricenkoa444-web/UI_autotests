from element.base_element import BaseElement
import allure

class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return 'image'


