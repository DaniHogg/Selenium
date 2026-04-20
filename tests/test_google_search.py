import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_google_search(browser):
    browser.get("https://www.google.com")
    time.sleep(1)

    # Accept prompt if appears
    try:
        agree = browser.find_element(By.XPATH, "//button/div[normalize-space()='I agree' or normalize-space()='Agree']")
        agree.click()
        time.sleep(1)
    except Exception:
        pass

    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Selenium automation with pytest")
    search_box.send_keys(Keys.RETURN)

    assert "Selenium" in browser.title
