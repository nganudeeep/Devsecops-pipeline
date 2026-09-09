from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "service-a",
    }


def test_get_message():
    response = client.get("/api/v1/message")

    assert response.status_code == 200
    assert response.json() == {
        "service": "service-a",
        "message": "Hello from Service A",
    }