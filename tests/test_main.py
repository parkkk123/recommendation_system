from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_features():
    response = client.get("/features?user_id=1")
    assert response.status_code == 200
    assert len(response.json()["features"][0]["histories"]) != 0

def test_get_OnlyItems():
    response = client.get("/recommendations?user_id=18")
    assert response.status_code == 200
    assert len(response.json()["items"]) != 0

def test_get_Item_wMetadata():
    response = client.get("/recommendations?user_id=18&returnMetadata=true")
    assert response.status_code == 200
    assert isinstance(response.json()["items"][0]["id"],int)
    assert isinstance(response.json()["items"][0]["title"],str)
    assert isinstance(response.json()["items"][0]["genres"],str)

def test_boundary_features():
    response = client.get("/features?user_id=weio")
    assert response.status_code == 422

def test_boundary_Item_wMetadata():
    response = client.get("/recommendations?user_id=test&returnMetadata=hi")
    assert response.status_code == 422

def test_get_OnlyItems():
    response = client.get("/recommendations?user_id=dfi")
    assert response.status_code == 422