"""Dashboard badge tests — verify that CI status cards carry a visible
freshness badge so reviewers can see whether results are current."""

from selenium.webdriver.common.by import By

from pages.dashboard_page import DashboardPage
from conftest import site_url


def test_dashboard_cards_have_status_badge(browser):
    """Each rendered CI card should include a freshness badge (Fresh or Stale)."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    cards = page.project_cards()
    assert cards, "No project cards found — JS render may have failed"
    for card in cards:
        badges = card.find_elements(By.CSS_SELECTOR, ".badge")
        assert badges, f"Card '{card.get_attribute('data-project-id')}' has no status badge"
        badge_text = " ".join(b.text for b in badges).strip()
        assert badge_text, "Badge element found but has no visible text"


def test_dashboard_brand_link_returns_home(browser):
    """Clicking the brand link from the dashboard should return to the home page."""
    page = DashboardPage(browser)
    page.open(site_url("dashboard.html"))
    brand = page.wait_for_element((By.CSS_SELECTOR, "a.brand"))
    brand.click()
    assert "dashboard" not in browser.current_url.lower(), (
        "Brand link did not navigate away from dashboard"
    )
