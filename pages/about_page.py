from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):
    """Page object for the About Me page (about.html)."""

    HEADING = (By.CSS_SELECTOR, "header h1")
    KICKER = (By.CSS_SELECTOR, "header .kicker")
    MAIN_CONTENT = (By.CSS_SELECTOR, "main.shell")

    def open(self, base_url: str):
        self.navigate(base_url)

    def heading_text(self) -> str:
        return self.wait_for_element(self.HEADING).text

    def kicker_text(self) -> str:
        return self.wait_for_element(self.KICKER).text

    def main_content(self):
        return self.wait_for_element(self.MAIN_CONTENT)
