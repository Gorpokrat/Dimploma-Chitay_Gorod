def test_api_create_order():
     token = "<valid_token>"  # Получите токен через авторизацию или фикстуру.
     url = "https://www.chitai-gorod.ru/api/order"
     headers = {"Authorization": f"Bearer {token}"}
     payload = {
         "items": [{"product_id": 12345, "quantity":1}],
         "delivery_address": "г. Москва, ул. Ленина д.1",
         "payment_method": "card"
     }
     
     response = requests.post(url, json=payload, headers=headers)
     assert response.status_code == 201
     data = response.json()
     assert data["order_id"] is not None
