def test_api_login_invalid():
     url = "https://www.chitai-gorod.ru/api/auth/login"
     payload = {
         "email": "testuser@example.com",
         "password": "wrong_password"
     }
     
     response = requests.post(url, json=payload)
     assert response.status_code == 401
     data = response.json()
     assert data["error"] == "Invalid credentials"
