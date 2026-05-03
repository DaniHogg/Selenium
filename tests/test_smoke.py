"""Smoke tests — verify that the main portfolio site pages load and return
the expected document titles.  These are the fastest tests in the suite
and act as a baseline signal for whether the deployment is healthy."""

from conftest import site_url


def test_home_page_loads(browser):
    browser.get(site_url())
    assert "Daniel Hogg" in browser.title


def test_portfolio_page_loads(browser):
    browser.get(site_url("portfolio.html"))
    assert "Automation Projects" in browser.title


def test_dashboard_page_loads(browser):
    browser.get(site_url("dashboard.html"))
    assert "Results" in browser.title


def test_about_page_loads(browser):
    browser.get(site_url("about.html"))
    assert "About" in browser.title
