import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver() -> WebDriver:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'капитанская'.")
    def test_by_name(self, driver):
        driver.get("https://www.chitai-gorod.ru")
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("капитанская")
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
        assert "капитанская" in driver.find_element(By.CLASS_NAME, "search-title").text

    @allure.title("Поиск автора")
    @allure.description("Тест проверяет возможность поиска автора 'пушкин'.")
    def test_by_name_author(self, driver):
        driver.get("https://www.chitai-gorod.ru")
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("капитанская")
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
        assert "капитанская" in driver.find_element(By.CLASS_NAME, "search-title").text

    @allure.title("Поиск книги на английском")
    @allure.description("Тест проверяет поиск книги с использование английского названия")
    def test_by_name_language_english(self, driver):
        driver.get("https://www.chitai-gorod.ru")
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("капитанская")
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
        assert "капитанская" in driver.find_element(By.CLASS_NAME, "search-title").text

    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использование символов вместо названия")
    def test_negative_by_symbols(self, driver):
        driver.get("https://www.chitai-gorod.ru")
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("капитанская")
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
        assert "не дал результатов" in driver.find_element(By.CLASS_NAME, "search-title").text

    @allure.title("Поиск книги на тайском языке")
    @allure.description("Тест проверяет поиск книги с использование тайских символов в названии")
    def test_negative_by_language_thai(self, driver):
        driver.get("https://www.chitai-gorod.ru")
        search_field = driver.find_element(By.NAME, "search")
        search_field.clear()
        search_field.send_keys("капитанская")
        driver.find_element(By.CLASS_NAME, "search-form__icon-search").click()
        WebDriverWait(driver, 40).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "search-title"), "капитанская"))
        assert "капитанская" in driver.find_element(By.CLASS_NAME, "search-title").text