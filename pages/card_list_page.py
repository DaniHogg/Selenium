from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CardListPage(BasePage):
    """Shared base for pages that render a hero heading/kicker plus a grid of
    project cards injected by JS after a fetch() call completes.

    Subclasses (e.g. DashboardPage, PortfolioPage) only need to set
    ``CARDS_CONTAINER`` and ``CARD_ARTICLE`` to the locators for their own
    card grid — everything else is identical between them.
    """

    HEADING = (By.CSS_SELECTOR, "header h1")
    KICKER = (By.CSS_SELECTOR, "header .kicker")

    # Subclasses must override these with their page-specific locators.
    CARDS_CONTAINER = None
    CARD_ARTICLE = None

    def open(self, url: str):
        self.navigate(url)

    def heading_text(self) -> str:
        return self.wait_for_element(self.HEADING).text

    def kicker_text(self) -> str:
        return self.wait_for_element(self.KICKER).text

    def cards_container(self):
        return self.wait_for_element(self.CARDS_CONTAINER)

    def project_cards(self):
        """Wait for JS-rendered cards to appear."""
        return self._wait.until(EC.presence_of_all_elements_located(self.CARD_ARTICLE))
