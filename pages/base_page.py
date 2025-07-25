
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()
    
    def get_element_text(self, locator):
        element = self.wait_for_element(locator)
        return element.text
    
    def open_url(self, url):
        self.driver.get(url)
