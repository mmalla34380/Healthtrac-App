from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_add_data():
    response = client.post("/add-data", json={
        "patient_name": "John",
        "heart_rate": 110,
        "blood_pressure": "120/80"
    })
    assert response.status_code == 200
