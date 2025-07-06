import pytest
import requests
from config.settings import API_URL, TOKEN

def test_api_login():
    url = f"{API_URL}/auth/login"
    payload = {
        "email": "testuser@example.com",
        "password": "correct_password"
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_api_search():
    url = f"{API_URL}/search"
    params = {"query": "Мастер и Маргарита"}
    
    response = requests.get(url, params=params)
    
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["results"], list)
