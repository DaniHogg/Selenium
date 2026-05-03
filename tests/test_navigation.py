"""Navigation tests — confirm that the top-nav links are present and functional
on the home page, and that clicking them lands on the expected destination."""

from selenium.webdriver.common.by import By

from conftest import site_url
from pages.home_page import HomePage


def test_nav_brand_link_visible(browser):
    page = HomePage(browser)
    page.open(site_url())
    brand = page.wait_for_element((By.CSS_SELECTOR, "a.brand"))
    assert brand.is_displayed()


def test_nav_links_displayed(browser):
    page = HomePage(browser)
    page.open(site_url())
    links = page.nav_links()
    assert len(links) >= 3, "Expected at least 3 nav links (brand + pages)"
    for link in links:
        assert link.is_displayed()


def test_navigate_to_portfolio(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("Automation Projects")
    assert "portfolio" in browser.current_url.lower()


def test_navigate_to_about(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("About")
    assert "about" in browser.current_url.lower()


def test_navigate_to_dashboard(browser):
    page = HomePage(browser)
    page.open(site_url())
    page.click_nav_link("Test Results")
    assert "dashboard" in browser.current_url.lower()
