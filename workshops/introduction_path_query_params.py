from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "root"}


@app.get("/items/{item_id}")
def read_root(item_id: int, q: str = None):
    # Service to your users
    return {"item_id": item_id, "q": q}
