"""Dashboard page tests — verify that the Live Test Results page renders
its static content and that CI status cards are injected by JavaScript."""

import pytest
from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage
from conftest import site_url


@pytest.mark.regression
def test_dashboard_heading(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    assert "Live Automation Results" in page.heading_text()


@pytest.mark.regression
def test_dashboard_kicker(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    assert page.kicker_text() != ""


@pytest.mark.regression
def test_dashboard_cards_container_present(browser):
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    container = page.cards_container()
    assert container.is_displayed()


@pytest.mark.regression
def test_dashboard_project_cards_rendered(browser):
    """Confirm that JavaScript fetches the project index and renders CI cards."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()
    assert len(cards) >= 1, "Expected at least one CI status card to be rendered by JS"


@pytest.mark.regression
def test_dashboard_details_links_target_project_page(browser):
    """Detail links should navigate to the project detail route with query id."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()

    links = cards[0].find_elements(By.CSS_SELECTOR, "a")
    assert links, "Expected at least one action link on dashboard card"
    href = links[0].get_attribute("href")
    assert "project.html?project=" in href
