from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_example_endpoint():
    response = client.get("/api/v1/example")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}  # Adjust based on actual response structure

def test_example_post_endpoint():
    response = client.post("/api/v1/example", json={"name": "Test"})
    assert response.status_code == 201
    assert response.json() == {"name": "Test", "message": "Created successfully"}  # Adjust based on actual response structure