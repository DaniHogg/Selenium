"""Portfolio page tests — verify that the Automation Projects page renders
its static heading content and that the JS-injected project cards appear."""

import pytest

from pages.portfolio_page import PortfolioPage
from conftest import site_url


@pytest.mark.regression
def test_portfolio_heading(browser):
    page = PortfolioPage(browser)
    page.open(site_url("portfolio.html"))
    assert "Automation" in page.heading_text()


@pytest.mark.regression
def test_portfolio_kicker(browser):
    page = PortfolioPage(browser)
    page.open(site_url("portfolio.html"))
    assert page.kicker_text() != ""


@pytest.mark.regression
def test_portfolio_cards_container_present(browser):
    page = PortfolioPage(browser)
    page.open(site_url("portfolio.html"))
    container = page.cards_container()
    assert container.is_displayed()


@pytest.mark.regression
def test_portfolio_project_cards_rendered(browser):
    """Confirm that JavaScript successfully fetches and renders project cards."""
    page = PortfolioPage(browser)
    page.open(site_url("portfolio.html"))
    cards = page.project_cards()
    assert len(cards) >= 1, "Expected at least one project card to be rendered by JS"
