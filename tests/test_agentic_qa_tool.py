"""Agentic QA Tool page content tests — verify that the project page renders
its heading and main content sections correctly."""

import pytest

from pages.agentic_qa_tool_page import AgenticQaToolPage
from conftest import site_url


@pytest.mark.regression
def test_agentic_qa_tool_title(browser):
    page = AgenticQaToolPage(browser)
    page.open(site_url("agentic-qa-tool.html"))
    assert "Agentic QA Tool" in page.title


@pytest.mark.regression
def test_agentic_qa_tool_heading(browser):
    page = AgenticQaToolPage(browser)
    page.open(site_url("agentic-qa-tool.html"))
    assert "Agentic QA Tool" in page.heading_text()


@pytest.mark.regression
def test_agentic_qa_tool_kicker(browser):
    page = AgenticQaToolPage(browser)
    page.open(site_url("agentic-qa-tool.html"))
    assert page.kicker_text() != ""


@pytest.mark.regression
def test_agentic_qa_tool_main_content_present(browser):
    page = AgenticQaToolPage(browser)
    page.open(site_url("agentic-qa-tool.html"))
    assert page.main_content().is_displayed()
