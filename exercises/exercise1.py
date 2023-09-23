"""
Objectvie: In this exercise, you'll create an endpoint in FastAPI application that simulates and advance search functionality for a food store.
The search should consider multiple optional query parameters, such as type, name, grams, Kcal, expire_date.

Steps:

1. Set up: We need to install fastapi and uvicorn (venv recommended)
2. Create a FastAPI application (main.py, foodstore.py)
3. Define the search endpoint
Create a new endpoint `GET /search` that accepts the following optional query parameters:
    * type (str)
    * name (str)
    * Grams (int)
    * Kcal (int)
    * expire_date (str)
4. Tests
    127.0.0.1/type
    Input type -> {"type": ["beef", "vegetals", "poulty"] }
    127.0.0.1/name
    Input name -> {"name": ["apple", "banana", "eggs"] }
    127.0.0.1/...
    Input Grams -> {"Grams": ["90", "120", "200"] }
    Input Kcal -> {"Kcal": ["100", "150", "90"] }
    Input expire_date -> {"expire_date": ["2023-09-23", "2023-09-10", "2023-09-11"] }

"""
from typing import List, Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/search/")
def search_foods(
    type: Optional[str] = None,
    name: Optional[str] = None,
    grams: Optional[str] = None,
    kcal: Optional[str] = None,
    expire_date: Optional[str] = None,
) -> List[dict]:
    # This is just a ock data for the sake of this exercise
    foods = [
        {
            "type": "vegetables",
            "name": "apple",
            "grams": "50",
            "kcal": "45",
            "expire_date": "2023-09-23",
        },
        {
            "type": "vegetables",
            "name": "banana",
            "grams": "46",
            "kcal": "90",
            "expire_date": "2023-09-22",
        },
        {
            "type": "poultry",
            "name": "chicken breast",
            "grams": "66",
            "kcal": "200",
            "expire_date": "2023-09-10",
        },
        {
            "type": "poultry",
            "name": "eggs",
            "grams": "55",
            "kcal": "170",
            "expire_date": "2023-09-10",
        },
        {
            "type": "vegetables",
            "name": "toffu",
            "grams": "44",
            "kcal": "159",
            "expire_date": "2023-09-10",
        },
    ]

    if type:
        foods = [food for food in foods if type.lower() in food["type"].lower()]
    if name:
        foods = [food for food in foods if name.lower() in food["name"].lower()]
    if grams:
        foods = [food for food in foods if grams.lower() in food["grams"].lower()]
    if kcal:
        foods = [food for food in foods if kcal.lower() in food["kcal"].lower()]
    if expire_date:
        foods = [
            food for food in foods if expire_date.lower() in food["expire_date"].lower()
        ]

    return foods
