def test_checkout_process(driver):
    driver.get("https://www.chitai-gorod.ru/cart")
    
    checkout_button_locator = (By.CSS_SELECTOR, ".btn-checkout")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(checkout_button_locator)).click()
    
    # Заполнение формы заказа (пример)
    name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "name")))
    name_input.send_keys("Иван Иванов")
    
    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.send_keys("+79991234567")
    
    # Отправка формы
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-order")
    submit_button.click()
    
    # Проверка подтверждения заказа
    confirmation_locator = (By.CSS_SELECTOR, ".order-confirmation")
    confirmation_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(confirmation_locator))
    assert "Спасибо за заказ" in confirmation_message.text
