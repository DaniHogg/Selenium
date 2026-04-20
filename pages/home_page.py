from selenium.webdriver.common.by import By


class HomePage:
    URL = "https://www.python.org"
    DOCS_LINK = (By.XPATH, "//a[@href='/docs/']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_docs(self):
        self.driver.find_element(*self.DOCS_LINK).click()
