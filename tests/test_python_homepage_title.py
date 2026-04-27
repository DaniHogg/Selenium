from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test that checks the title of the Python homepage
def test_python_homepage_title(browser):
    browser.get("https://www.python.org")
    WebDriverWait(browser, 10).until(EC.title_contains("Python"))
    assert "Python" in browser.title  # Assert that 'Python' is in the page title
