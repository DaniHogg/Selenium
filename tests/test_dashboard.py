"""Dashboard page tests — verify that the Live Test Results page renders
its static content and that CI status cards are injected by JavaScript."""

from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage
from conftest import site_url


def test_dashboard_heading(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    assert "Live Automation Results" in page.heading_text()


def test_dashboard_kicker(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    assert page.kicker_text() != ""


def test_dashboard_cards_container_present(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    container = page.cards_container()
    assert container.is_displayed()


def test_dashboard_project_cards_rendered(browser):
    """Confirm that JavaScript fetches the project index and renders CI cards."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()
    assert len(cards) >= 1, "Expected at least one CI status card to be rendered by JS"


def test_dashboard_cards_show_freshness_status(browser):
    """Each card should expose a freshness label (Fresh or Stale)."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()

    for card in cards:
        status_nodes = card.find_elements(By.CSS_SELECTOR, "p")
        status_text = " ".join(node.text for node in status_nodes)
        assert ("Fresh" in status_text) or ("Stale" in status_text), (
            f"Expected freshness label in card text, got: {status_text!r}"
        )


def test_dashboard_details_links_target_project_page(browser):
    """Detail links should navigate to the project detail route with query id."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()

    links = cards[0].find_elements(By.CSS_SELECTOR, "a")
    assert links, "Expected at least one action link on dashboard card"
    href = links[0].get_attribute("href")
    assert "project.html?project=" in href
