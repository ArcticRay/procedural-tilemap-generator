import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_generate_map_success():
    resp = client.post(
        "/generate_map/", json={"width": 4, "height": 4, "biome": "desert"}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "map" in data
    assert len(data["map"]) == 4
    assert all(len(row) == 4 for row in data["map"])


@pytest.mark.parametrize(
    "bad_payload",
    [
        {},
        {"width": "16", "height": 16, "biome": "forest"},
        {"width": -1, "height": 5, "biome": "forest"},
    ],
)
def test_generate_map_errors(bad_payload):
    resp = client.post("/generate_map/", json=bad_payload)
    assert resp.status_code == 422


def test_generate_map_get_success():
    resp = client.get("/generate_map/?width=4&height=4&biome=desert")
    assert resp.status_code == 200
    data = resp.json()
    assert "map" in data and len(data["map"]) == 4


@pytest.mark.parametrize(
    "qs",
    [
        "",
        "?width=0&height=5&biome=forest",
        "?width=5&height=5&biome=void",
    ],
)
def test_generate_map_get_errors(qs):
    resp = client.get(f"/generate_map/{qs}")
    assert resp.status_code == 422
