from selenium.webdriver.common.by import By

from pages.card_list_page import CardListPage


class DashboardPage(CardListPage):
    """Page object for the Live Test Results dashboard (dashboard.html)."""

    ACTIVE_PROJECTS_HEADING = (By.XPATH, "//section//h2[contains(text(), 'Active Automation Projects')]")
    CARDS_CONTAINER = (By.ID, "project-cards")
    # Cards are injected by JS after a fetch() call completes.
    CARD_ARTICLE = (By.CSS_SELECTOR, "#project-cards article.card")
