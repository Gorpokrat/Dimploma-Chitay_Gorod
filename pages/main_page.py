from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="search"]')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    CART_ICON = (By.CSS_SELECTOR, '.header-cart')

    def search_for(self, query):
        self.wait_for_element(self.SEARCH_INPUT).send_keys(query)
        self.click_element(self.SEARCH_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART_ICON)
