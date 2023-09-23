"""
Request body
reponse model
Dependency injection
"""
import time
from typing import Optional

from fastapi import Depends, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


def get_db():
    time.sleep(1)
    db = "Some db uri"
    return db


@app.get("/")
def root():
    return {"Hello": "root"}


# Request body
@app.post("/items/")
def create_item(item: Item):
    # Perform any db actions in here
    time.sleep(2)
    return item


# reponse model
@app.get("/items/{item_id}")
def read_item(item_id: int, response_model=Item):
    # Perform any db actions in here
    time.sleep(1)
    return Item(name="Item", price=100.11)


# Dependency injection
@app.get("/db/")
def read_db(db: Optional[str] = Depends(get_db)):
    return {"db": db}
