import requests

def test_api_login():
    url = "https://www.chitai-gorod.ru/api/auth/login"
    payload = {
        "email": "testuser@example.com",
        "password": "correct_password"
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "token" in data
