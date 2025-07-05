def test_add_product_to_cart(driver):
    driver.get("https://www.chitai-gorod.ru")
    main_page = MainPage(driver)
    main_page.search_for("Мастер и Маргарита")
    
    # Переход на страницу товара (пример)
    product_link_locator = (By.CSS_SELECTOR, ".product-card a")
    product_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(product_link_locator))
    product_link.click()
    
    product_page = ProductPage(driver)
    product_page.add_to_cart()
    
    # Проверка появления сообщения или значка корзины
    cart_count_locator = (By.CSS_SELECTOR, ".cart-count")
    cart_count = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(cart_count_locator, "1"))
    assert cart_count
