import time
from selenium.webdriver.common.by import By

# Test that checks the presence of the Downloads menu
def test_python_downloads_menu(browser):
    browser.get("https://www.python.org")
    time.sleep(1)
    # Find the Downloads menu by its link text
    downloads_menu = browser.find_element(By.LINK_TEXT, "Downloads")
    assert downloads_menu.is_displayed()  # Assert the menu is visible
