import fastapi
import uvicorn
from pydantic import BaseModel

app = fastapi.FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get('/')
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World"}

@app.get('/items/{item_id}')
async def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}

@app.post('/items/')
async def create_item(item: Item) -> dict[str, Item]:
    return {"item": item}

@app.get('/users/{user_id}')
def get_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}

@app.post('/users/')
def create_user(user: dict) -> dict[str, dict]:
    return {"user": user}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)