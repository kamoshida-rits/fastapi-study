# from typing import Optional

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/items/")
# async def read_items(q: Optional[str] = None):

#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# ####################################################

# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")

# async def read_items(q: Optional[str] = Query('ho', min_length=3, max_length=50)):

#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# ####################################################

# from typing import List, Optional

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")

# async def read_items(q: Optional[List[str]] = Query(None)):

#     query_items = {"q": q}
#     return query_items

# ####################################################

# from typing import Optional

# from fastapi import FastAPI, Query

# app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         title="Query string",

#         description="Query string for the items to search in the database that have a good match",

#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# ####################################################

from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
