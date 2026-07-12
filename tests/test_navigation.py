"""Navigation tests — confirm that the top-nav links are present and functional
on the home page, and that clicking them lands on the expected destination."""

import pytest
from selenium.webdriver.common.by import By

from conftest import site_url
from pages.home_page import HomePage

# The top-nav (`nav.top-nav a`) contains the brand link plus the four page
# links, in DOM order. This is the full, exact set the live site renders.
EXPECTED_NAV_LINK_TEXTS = [
    "Daniel Hogg",
    "About Me",
    "Agentic QA Tool",
    "Automation Projects",
    "Test Results",
]


@pytest.mark.regression
def test_nav_brand_link_visible(browser):
    page = HomePage(browser)
    page.open(site_url())
    brand = page.wait_for_element((By.CSS_SELECTOR, "a.brand"))
    assert brand.is_displayed()


@pytest.mark.regression
def test_nav_links_displayed(browser):
    page = HomePage(browser)
    page.open(site_url())
    links = page.nav_links()
    assert len(links) == 5, "Expected exactly 5 nav links (brand + 4 page links)"
    for link in links:
        assert link.is_displayed()
    actual_texts = [link.text.strip() for link in links]
    assert actual_texts == EXPECTED_NAV_LINK_TEXTS


@pytest.mark.regression
def test_navigate_to_portfolio(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("Automation Projects")
    assert "portfolio" in browser.current_url.lower()


@pytest.mark.regression
def test_navigate_to_about(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("About")
    assert "about" in browser.current_url.lower()


@pytest.mark.regression
def test_navigate_to_dashboard(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("Test Results")
    assert "dashboard" in browser.current_url.lower()


@pytest.mark.regression
def test_navigate_to_agentic_qa_tool(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("Agentic QA Tool")
    assert "agentic-qa-tool" in browser.current_url.lower()
