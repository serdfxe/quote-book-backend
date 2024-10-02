from fastapi.testclient import TestClient

from app import app


client = TestClient(app)
client.headers["Content-Type"] = "application/json"
