from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Test that performs a search for 'pytest' on python.org
def test_python_search_pytest(browser):
    browser.get("https://www.python.org")
    wait = WebDriverWait(browser, 10)
    # Wait for search box to be interactive, then submit the query
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))
    search_box.send_keys("pytest")
    search_box.submit()
    # Wait for results page to load before asserting content
    wait.until(EC.url_contains("q=pytest"))
    assert "pytest" in browser.page_source
