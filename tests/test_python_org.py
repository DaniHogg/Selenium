from selenium.webdriver.common.by import By

from pages.home_page import HomePage


def test_python_org_title(browser):
    browser.get("https://www.python.org")

    assert "Python" in browser.title


def test_docs_link(browser):
    home_page = HomePage(browser)
    home_page.open()
    home_page.open_docs()
    assert "Documentation" in browser.title
