# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None


# @app.put("/items/{item_id}")

# async def update_item(item_id: int, item: Item, user: User):

#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

# ####################################################

from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_id}")
async def update_item(

    item_id: int, item: Item, user: User, importance: int = Body(...)

):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
