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
