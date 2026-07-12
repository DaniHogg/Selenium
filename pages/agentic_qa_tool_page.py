from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AgenticQaToolPage(BasePage):
    """Page object for the Agentic QA Tool project page (agentic-qa-tool.html)."""

    HEADING = (By.CSS_SELECTOR, "header h1")
    KICKER = (By.CSS_SELECTOR, "header .kicker")
    MAIN_CONTENT = (By.CSS_SELECTOR, "main.shell")

    def open(self, url: str):
        self.navigate(url)

    def heading_text(self) -> str:
        return self.wait_for_element(self.HEADING).text

    def kicker_text(self) -> str:
        return self.wait_for_element(self.KICKER).text

    def main_content(self):
        return self.wait_for_element(self.MAIN_CONTENT)
