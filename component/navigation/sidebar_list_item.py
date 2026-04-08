from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from typing import Pattern

from element.button import Button
from element.icon import Icon
from element.text import Text


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f"{identifier}-drawer-list-item-icon", "Sidebar list item icon")
        self.title = Text(page, f"{identifier}-drawer-list-item-title-text", "Sidebar list item title")
        self.button = Button(page, f'{identifier}-drawer-list-item-button', "Sidebar list item button")


    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)