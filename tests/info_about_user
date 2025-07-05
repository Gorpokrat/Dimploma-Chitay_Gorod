def test_api_get_user_info():
     token = "<valid_token>"
     url = "https://www.chitai-gorod.ru/api/user/profile"
     headers = {"Authorization": f"Bearer {token}"}
     
     response = requests.get(url, headers=headers)
     
     assert response.status_code == 200
     data = response.json()
     assert data["email"] == "testuser@example.com"
