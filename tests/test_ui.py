import pytest 
import allure 
from selenium import webdriver 

from pages.main_page import MainPage 

@pytest.fixture(scope='session') 
def driver(): 
    driver = webdriver.Chrome()  # или настройка headless при необходимости 
    yield driver 
    driver.quit() 

@allure.feature('UI Tests') 
def test_open_main_page(driver): 
    with allure.step("Открываем главную страницу"): 
        driver.get('https://www.chitai-gorod.ru') 
        assert 'Читай-город' in driver.title 

@allure.feature('UI Tests') 
def test_search_product(driver): 
    page = MainPage(driver) 
    with allure.step("Ищем книгу 'Мастер и Маргарита'"): 
        page.search_for('Мастер и Маргарита') 
        
        # Можно добавить проверку появления результатов поиска или перехода на страницу товара.
        
        results_locator = (By.CSS_SELECTOR, '.search-results')  # пример локатора результатов поиска
        
        results = page.wait_for_element(results_locator)
        assert results.is_displayed()
