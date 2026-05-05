"""About page content tests — verify that the About Me page renders its
heading and main content sections correctly."""

from pages.about_page import AboutPage
from conftest import site_url


def test_about_heading(browser):
    page = AboutPage(browser)
    page.open(site_url("about.html"))
    assert "QA Automation" in page.heading_text()


def test_about_kicker(browser):
    page = AboutPage(browser)
    page.open(site_url("about.html"))
    assert "About" in page.kicker_text()


def test_about_main_content_present(browser):
    page = AboutPage(browser)
    page.open(site_url("about.html"))
    assert page.main_content().is_displayed()
