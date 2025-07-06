def test_search_product(driver):
    main_page = MainPage(driver)
    main_page.open_url("https://www.chitai-gorod.ru")
    main_page.search_for("Мастер и Маргарита")
    # Проверка наличия результатов
    results_locator = (By.CSS_SELECTOR, ".search-results")
    results = WebDriverWait(driver, 10).until(EC.presence_of_element_located(results_locator))
    assert results.is_displayed()
