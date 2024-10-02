import json
from . import client


def test_get_quotes():
    response = client.get("/quotes")
    
    assert response.status_code == 200, "Статус код должен быть 200."
    assert isinstance(response.json(), list), "Вернулся не список."

def test_add_quote():
    new_quote_text = "Это новая цитата."
    response = client.post("/quotes/", params={"quote_text": new_quote_text})
    
    new_quote = response.json()

    assert response.status_code == 201, "Статус код должен быть 201."
    assert new_quote["text"] == new_quote_text, "Не совпал текст отправляемого и текст возвращаемого."
    
    get_response = client.get(f"/quotes/{new_quote['id']}", params={"id": new_quote["id"]})

    assert get_response.json() == new_quote, "Не правильно сохранилось в БД."

def test_delete_quote_success():
    response = client.post("/quotes/", params={"quote_text": "1"})
    response = client.post("/quotes/", params={"quote_text": "2"})
    response = client.post("/quotes/", params={"quote_text": "3"})

    response = client.delete("/quotes/3")
    
    assert response.status_code == 204, "Статус код должен быть 204."

def test_delete_quote_not_found():
    response = client.delete("/quotes/999")
    
    assert response.status_code == 404, "Статус код должен быть 404."

def test_put_quote_success():
    response = client.put("/quotes/1", params={"quote_id": 1, "quote_text": "22"})
    
    assert response.status_code == 201, "Статус код должен быть 201"
    assert response.json() == {"id": 1, "text": "22"}, "Не правильно обновился текст цитаты."

def test_delete_quote_not_found():
    response = client.delete("/quotes/999")
    
    assert response.status_code == 404, "Статус код должен быть 404."

def test_search_quote():
    client.post("/quotes/", params={"quote_text": "a"})
    client.post("/quotes/", params={"quote_text": "aa"})
    client.post("/quotes/", params={"quote_text": "aaa"})

    response = client.get("/quotes/search/", params={"keyword": "aa"})

    quotes = response.json()

    print(quotes)

    assert [i["text"] for i in quotes] == ["aa", "aaa"], "Смотреть тест."
