import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Portfolio site base URL components — mirrors the Playwright conftest pattern.
# In CI: BASE_URL=https://danihogg.github.io  SITE_BASE_PATH=/qa-portfolio-livesite
# Locally: defaults to the live site (no local server required for read-only tests).
_BASE_URL = os.environ.get("BASE_URL", "https://danihogg.github.io").rstrip("/")
_SITE_BASE_PATH = os.environ.get("SITE_BASE_PATH", "/qa-portfolio-livesite").rstrip("/")


def site_url(path: str = "") -> str:
    """Return an absolute URL for a portfolio-site-relative path.

    Examples::
        site_url()              -> "https://danihogg.github.io/qa-portfolio-livesite"
        site_url("portfolio.html") -> ".../qa-portfolio-livesite/portfolio.html"
    """
    if path and not path.startswith("/"):
        path = "/" + path
    return _BASE_URL + _SITE_BASE_PATH + path


@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
