from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PortfolioPage(BasePage):
    """Page object for the Automation Projects page (portfolio.html)."""

    HEADING = (By.CSS_SELECTOR, "header h1")
    KICKER = (By.CSS_SELECTOR, "header .kicker")
    PROJECTS_HEADING = (By.XPATH, "//section//h2[contains(text(), 'Projects')]")
    CARDS_CONTAINER = (By.ID, "portfolio-cards")
    # Cards are injected by JS; wait for at least one article to appear.
    CARD_ARTICLE = (By.CSS_SELECTOR, "#portfolio-cards article.card")

    def open(self, base_url: str):
        self.navigate(base_url)

    def heading_text(self) -> str:
        return self.wait_for_element(self.HEADING).text

    def kicker_text(self) -> str:
        return self.wait_for_element(self.KICKER).text

    def cards_container(self):
        return self.wait_for_element(self.CARDS_CONTAINER)

    def project_cards(self):
        """Wait for JS-rendered project cards to appear."""
        return self._wait.until(EC.presence_of_all_elements_located(self.CARD_ARTICLE))
