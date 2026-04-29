from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_google_search(browser):
    browser.get("https://www.google.com")
    wait = WebDriverWait(browser, 10)

    # Accept consent prompt if present
    try:
        agree = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button/div[normalize-space()='I agree' or normalize-space()='Agree']")
            )
        )
        agree.click()
    except Exception:
        pass

    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("Selenium automation with pytest")
    search_box.send_keys(Keys.RETURN)

    wait.until(EC.title_contains("Selenium"))
    assert "Selenium" in browser.title
