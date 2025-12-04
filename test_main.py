from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_tokenize_valid_text():
    input_data = {"text": "hello"}
    response = client.post("/tokenize", json=input_data)
    assert response.status_code == 200
    expected_checksum = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    assert response.json() == {"checksum": expected_checksum}

def test_tokenize_empty_text():
    input_data = {"text": ""}
    response = client.post("/tokenize", json=input_data)
    assert response.status_code == 200
    expected_checksum = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert response.json() == {"checksum": expected_checksum}

def test_tokenize_missing_text_field():
    input_data = {}
    response = client.post("/tokenize", json=input_data)
    # FastAPI returns a 422 for validation error
    assert response.status_code == 422
    assert "detail" in response.json()