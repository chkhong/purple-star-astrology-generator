from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_run():
  response = client.get("/")
  assert response.json() == {"message": "App is running..."}