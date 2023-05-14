from typing import Union
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return Response('<h1 style="text-align:center">Hello</h1>')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
