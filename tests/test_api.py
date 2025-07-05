import requests 
import pytest 
import allure 

from config.settings import API_URL, TOKEN 

@allure.feature('API Tests') 
def test_get_user_info(): 
    headers = {'Authorization': f'Bearer {TOKEN}'} 
    response = requests.get(f"{API_URL}/user/info", headers=headers) 
    assert response.status_code == 200 
    data = response.json() 
    assert 'id' in data and 'name' in data 

@allure.feature('API Tests') 
def test_create_resource(): 
    payload = {"name": "test", "value": 123} 
    headers = {'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'} 
    response = requests.post(f"{API_URL}/resources", json=payload, headers=headers) 
    assert response.status_code == 201 
