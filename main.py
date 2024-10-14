from typing import Union

from fastapi import FastAPI

# Fast API 객체 생성
app = FastAPI()

# localhost:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}