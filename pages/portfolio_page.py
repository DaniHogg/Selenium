from selenium.webdriver.common.by import By

from pages.card_list_page import CardListPage


class PortfolioPage(CardListPage):
    """Page object for the Automation Projects page (portfolio.html)."""

    PROJECTS_HEADING = (By.XPATH, "//section//h2[contains(text(), 'Projects')]")
    CARDS_CONTAINER = (By.ID, "portfolio-cards")
    # Cards are injected by JS; wait for at least one article to appear.
    CARD_ARTICLE = (By.CSS_SELECTOR, "#portfolio-cards article.card")
