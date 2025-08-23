import pytest
from fastapi.testclient import TestClient
from code.main import app

client = TestClient(app)

def test_get():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"message": "GET method called"}

def test_post():
	data = {"key": "value"}
	response = client.post("/", json=data)
	assert response.status_code == 200
	assert response.json()["message"] == "POST method called"
	assert response.json()["data"] == data

def test_put():
	data = {"key": "value"}
	response = client.put("/", json=data)
	assert response.status_code == 200
	assert response.json()["message"] == "PUT method called"
	assert response.json()["data"] == data

def test_delete():
	response = client.delete("/")
	assert response.status_code == 200
	assert response.json() == {"message": "DELETE method called"}

def test_patch():
	data = {"key": "patched"}
	response = client.patch("/", json=data)
	assert response.status_code == 200
	assert response.json()["message"] == "PATCH method called"
	assert response.json()["data"] == data

def test_options():
	response = client.options("/")
	assert response.status_code == 200
	assert "Allow" in response.headers

def test_head():
	response = client.head("/")
	assert response.status_code == 200
