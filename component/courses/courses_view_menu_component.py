from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.button import Button


class CoursesViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, "course-view-menu-button", "Menu button")
        self.edit_item = Button(page, "course-view-edit-menu-item", "Edit menu item")
        self.delete_item = Button(page, "course-view-delete-menu-item", "Delete menu item")

    def click_edit_course(self, index: int):
        self.menu_button.nth(index).click()

        self.edit_item.nth(index).to_be_visible()
        self.edit_item.nth(index).click()

    def click_delete_course(self, index: int):
        self.menu_button.nth(index).click()

        self.delete_item.nth(index).to_be_visible()
        self.delete_item.nth(index).click()