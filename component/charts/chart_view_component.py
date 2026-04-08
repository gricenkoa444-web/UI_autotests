from playwright.sync_api import Page, expect
from component.base_component import BaseComponent
from element.text import Text


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', "Title chart")
        self.chart = Text(page, f'{identifier}-{chart_type}-chart', "Chart")

    def check_visible(self, title):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()
