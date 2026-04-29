from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Test that checks the presence of the Downloads menu
def test_python_downloads_menu(browser):
    browser.get("https://www.python.org")
    wait = WebDriverWait(browser, 10)
    # Wait until the Downloads link is visible in the nav bar
    downloads_menu = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Downloads")))
    assert downloads_menu.is_displayed()
