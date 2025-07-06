import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_search_product(driver):
    driver.get("https://www.chitai-gorod.ru")
    search_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.search-input"))
    )
    search_input.send_keys("Мастер и Маргарита")
    search_button = driver.find_element(By.CSS_SELECTOR, ".search-button")
    search_button.click()
    
    results_locator = (By.CSS_SELECTOR, ".search-results")
    results = WebDriverWait(driver, 10).until(EC.presence_of_element_located(results_locator))
    assert results.is_displayed()
