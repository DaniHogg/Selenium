import time
from selenium.webdriver.common.by import By

# Test that checks the title of the Python homepage
def test_python_homepage_title(browser):
    browser.get("https://www.python.org")
    time.sleep(1)  # Wait for the page to load
    assert "Python" in browser.title  # Assert that 'Python' is in the page title
