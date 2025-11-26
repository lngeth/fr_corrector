from fastapi.testclient import TestClient
from corrector_api.main import app

client = TestClient(app)

def test_correct_text():
  r = client.post("/correct_grammar_fr", json={
    "text": "Bojnour, je m'appelle Laurent"
  })
  assert r.status_code == 200
  assert r.json() == {"corrected_text": "Bonjour, je m'appelle Laurent"}
  