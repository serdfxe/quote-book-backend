from . import client


def test_hi():
    response = client.get("/hi")
    
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World!"}
