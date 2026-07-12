"""Smoke tests — verify that the main portfolio site pages load and return
the expected document titles.  These are the fastest tests in the suite
and act as a baseline signal for whether the deployment is healthy."""

import pytest

from conftest import site_url


@pytest.mark.smoke
def test_home_page_loads(browser):
    browser.get(site_url())
    assert "Daniel Hogg" in browser.title


@pytest.mark.smoke
def test_portfolio_page_loads(browser):
    browser.get(site_url("portfolio.html"))
    assert "Automation Projects" in browser.title


@pytest.mark.smoke
def test_dashboard_page_loads(browser):
    browser.get(site_url("dashboard.html"))
    assert "Results" in browser.title


@pytest.mark.smoke
def test_about_page_loads(browser):
    browser.get(site_url("about.html"))
    assert "About" in browser.title


@pytest.mark.smoke
def test_agentic_qa_tool_page_loads(browser):
    browser.get(site_url("agentic-qa-tool.html"))
    assert "Agentic QA Tool" in browser.title
