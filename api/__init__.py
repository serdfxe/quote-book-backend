from dataclasses import dataclass
from typing import List
from fastapi import APIRouter, Query


router = APIRouter(tags=["User"])


@dataclass
class Quote:
    id: int
    text: str
    author: str


@router.get("/hi")
async def hi_route():
    return {"msg": "Hello World!"}


@router.get("/quotes/")
async def get_quotes_route() -> list[Quote]:
    """Получение списка всех цитат."""
    ...

@router.get("/quotes/{quote_id}")
async def get_quote_route(quote_id: int) -> Quote:
    """Получение цитаты по ID."""
    ...

@router.post("/quotes/")
async def create_quote_route(quote_text: str) -> Quote:
    """Добавление новой цитаты."""
    ...

@router.put("/quotes/{quote_id}")
async def update_quote_route(quote_id: int, quote_text: str) -> Quote:
    """Обновление существующей цитаты по ID."""
    ...

@router.delete("/quotes/{quote_id}")
async def delete_quote_route(quote_id: int):
    """Удаление цитаты по ID."""
    ...

@router.get("/quotes/search/")
async def search_quotes_route(
    keyword: str | None = None
) -> list[Quote]:
    """Поиск цитат по ключевому слову.
    
    Параметры:
    - keyword: Опциональный параметр для фильтрации цитат по ключевому слову.
    """
    ...
