from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10


class BasePage:
    """Shared helpers for all portfolio-site page objects."""

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def navigate(self, url: str):
        self.driver.get(url)

    def wait_for_element(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    def wait_for_elements(self, locator):
        return self._wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    @property
    def title(self) -> str:
        return self.driver.title

    @property
    def current_url(self) -> str:
        return self.driver.current_url
