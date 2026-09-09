from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "service-b",
    }


def test_get_user():
    response = client.get("/api/v1/user")

    assert response.status_code == 200
    assert response.json() == {
        "service": "service-b",
        "user": {
            "id": 1,
            "name": "devops-user",
            "role": "engineer",
        },
    }