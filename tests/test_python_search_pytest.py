import time
from selenium.webdriver.common.by import By

# Test that performs a search for 'pytest' on python.org
def test_python_search_pytest(browser):
    browser.get("https://www.python.org")
    time.sleep(1)
    # Find the search input by its name attribute
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("pytest")
    search_box.submit()  # Submit the search form
    time.sleep(1)
    # Assert that the results page contains 'pytest' in the page source
    assert "pytest" in browser.page_source
