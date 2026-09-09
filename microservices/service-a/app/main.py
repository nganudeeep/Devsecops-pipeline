from fastapi import FastAPI

app = FastAPI(title="Service A")

# /health for Kubernetes health checks
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "service-a"}

# actual application endpoint
@app.get("/api/v1/message")
def get_message():
    return {
        "service": "service-a",
        "message": "Hello from Service A"
    }