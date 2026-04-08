from component.base_component import BaseComponent
from playwright.sync_api import Page, expect

from element.icon import Icon
from element.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f"{identifier}-empty-view-icon", "Empty view icon")
        self.title = Text(page, f"{identifier}-empty-view-title-text", "Empty view title")
        self.description = Text(page, f"{identifier}-empty-view-description-text", "Empty description")

    def check_visible(self, title: str, description: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)
