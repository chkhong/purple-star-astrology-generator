from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_run():
  response = client.get("/users")
  assert response.json() == {"router": "users"}