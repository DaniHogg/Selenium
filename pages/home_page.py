from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page object for the portfolio home page (index.html)."""

    NAV_LINKS = (By.CSS_SELECTOR, "nav.top-nav a")
    BRAND_LINK = (By.CSS_SELECTOR, "a.brand")
    HERO_KICKER = (By.CSS_SELECTOR, "header .kicker")
    CTA_BUTTONS = (By.CSS_SELECTOR, ".cta-row a.btn")
    HIGHLIGHT_CARDS = (By.CSS_SELECTOR, ".highlights .highlight-card")
    FEATURE_CARDS = (By.CSS_SELECTOR, ".cards .card")

    def open(self, base_url: str):
        self.navigate(base_url)

    def nav_links(self):
        return self.wait_for_elements(self.NAV_LINKS)

    def cta_buttons(self):
        return self.wait_for_elements(self.CTA_BUTTONS)

    def highlight_cards(self):
        return self.wait_for_elements(self.HIGHLIGHT_CARDS)

    def click_nav_link(self, link_text: str):
        for link in self.nav_links():
            if link_text.lower() in link.text.lower():
                link.click()
                return
        raise ValueError(f"Nav link containing '{link_text}' not found")
