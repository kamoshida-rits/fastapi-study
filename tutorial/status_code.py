from fastapi import FastAPI, status
from http import HTTPStatus
app = FastAPI()

# @app.post("/items/")
# @app.post("/items/", status_code=201)
# @app.post("/items/", status_code=status.HTTP_201_CREATED)
@app.post("/items/", status_code=HTTPStatus.CREATED)
async def create_item(name: str):
    return {"name": name}
