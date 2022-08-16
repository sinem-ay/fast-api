from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_inexistent_game():
    response = client.get("/games/3")
    assert response.status_code == 404


def test_add_game():
    response = client.post(
        "/game/",
        json={"id": 3, "game_name": "host_1", "game_type": "headset", "price": 50, "company": "test", "country": True})
    assert response.status_code == 201
    assert response.json() == {
        "id": 3,
        "game_name": "host_1",
        "game_type": "headset",
        "price": 50,
        "company": "test",
        "country": True
    }


def test_get():
    response = client.get("/games")
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "username": "customer_2",
            "item_name": "Macbook",
            "price": 6000,
            "item_stock": True
        },
        {
            "id": 2,
            "username": "customer_3",
            "item_name": "thinkpad",
            "price": 5000,
            "item_stock": True
        },
        {
            "id": 3,
            "username": "host_1",
            "item_name": "headset",
            "price": 50,
            "item_stock": True
        }
    ]


def test_delete_game():
    response = client.delete("/game/3")
    assert response.status_code == 200
