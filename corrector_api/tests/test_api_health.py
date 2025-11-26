from fastapi.testclient import TestClient
from fastapi import FastAPI
from corrector_api.main import app

client = TestClient(app)

def test_health_check():
  r = client.get("/health")
  assert r.status_code == 200
  assert r.json() == {"status": 'ok'}