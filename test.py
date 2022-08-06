from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get():
    response = client.get("/items")
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
    }
]

