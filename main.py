from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Creating schema/model
class Item(BaseModel):
    id: int
    username: str
    item_name: str
    price: int
    item_stock: bool

# Display a message with GET
@app.get('/')
def index():
    return {"message": "First message"}

# Display a greeting message to specified username
@app.get('/greet/{username}')
def greet_username(username: str):
    return {"message": f"Welcome {username}"}

# Display a greeting message to an optional username
@app.get('/greet')
def greet_optional_username(username: Optional[str] = "username"):
    return {"message": f"Welcome {username}"}

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {'name': item.item_name,
            'price': item.price,
            'available_stock': item.item_stock}

