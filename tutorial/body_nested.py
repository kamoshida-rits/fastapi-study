# from typing import Optional, Set


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

#     tags: Set[str] = set()



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# ####################################################


# from typing import Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Image(BaseModel):
#     url: str
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = []

#     image: Optional[Image] = None



# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results


# ####################################################

# from typing import Optional, Set

# from fastapi import FastAPI

# from pydantic import BaseModel, HttpUrl


# app = FastAPI()


# class Image(BaseModel):

#     url: HttpUrl

#     name: str


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()
#     image: Optional[Image] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# ####################################################

# from typing import List, Optional, Set

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()



# class Image(BaseModel):

#     url: HttpUrl
#     name: str



# class Item(BaseModel):

#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()

#     images: Optional[List[Image]] = None




# class Offer(BaseModel):

#     name: str
#     description: Optional[str] = None
#     price: float

#     items: List[Item]



# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer

# ####################################################

# from typing import List

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# @app.post("/images/multiple/")

# async def create_multiple_images(images: List[Image]):
#     for image in images:
#         image.url
#     return images

# ####################################################

from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights
