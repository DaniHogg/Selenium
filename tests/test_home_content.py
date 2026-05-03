"""Home page content tests — verify that the hero section, CTA buttons, and
highlight cards are rendered correctly after page load."""

from pages.home_page import HomePage
from conftest import site_url


def test_hero_kicker_visible(browser):
    page = HomePage(browser)
    page.open(site_url())
    kicker = page.wait_for_element(page.HERO_KICKER)
    assert "QA Automation Engineer" in kicker.text


def test_cta_buttons_present(browser):
    page = HomePage(browser)
    page.open(site_url())
    buttons = page.cta_buttons()
    assert len(buttons) >= 2, "Expected at least two CTA buttons in the hero"
    for btn in buttons:
        assert btn.is_displayed()


def test_highlight_cards_present(browser):
    page = HomePage(browser)
    page.open(site_url())
    cards = page.highlight_cards()
    assert len(cards) >= 2, "Expected highlight cards section with at least two entries"


def test_feature_cards_contain_links(browser):
    from selenium.webdriver.common.by import By
    page = HomePage(browser)
    page.open(site_url())
    link_rows = page.wait_for_elements((By.CSS_SELECTOR, ".cards .card .link-row a"))
    assert len(link_rows) >= 2, "Expected feature cards to contain at least two links"
    link_texts = [el.text for el in link_rows]
    assert any(link_texts), "Feature card links should have visible text"
