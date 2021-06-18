from typing import Optional, List


from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    x_token: Optional[List[str]] = Header(None),
):
    return {
        "User-Agent": user_agent,
        "accept-encoding": accept_encoding,
        "X-Token values": x_token,
    }
