from fastapi import FastAPI

app = FastAPI(title="Service B")


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "service-b"
    }


@app.get("/api/v1/user")
def get_user():
    return {
        "service": "service-b",
        "user": {
            "id": 1,
            "name": "devops-user",
            "role": "engineer"
        }
    }