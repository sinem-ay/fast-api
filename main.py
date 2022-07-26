from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()


# Creating schema/model item class with pydantic
class Item(BaseModel):
    id: int
    username: str
    item_name: str
    price: int
    item_stock: bool

    class Config:
        orm_mode = True  # Sql objects to json


db = SessionLocal()


@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    return db.query(models.Item).all()


@app.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_item(item_id: int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()

    return item


@app.post('/items', response_model=Item, status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    db_item = db.query(models.Item).filter(models.Item.item_name == item.item_name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models.Item(
        username=item.username,
        item_name=item.item_name,
        price=item.price,
        item_stock=item.item_stock
    )

    db.add(new_item)
    db.commit()

    return new_item


@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_item(item_id: int, item: Item):
    item_update = db.query(models.Item).filter(models.Item.id == item_id).first()

    item_update.username = item.username
    item_update.price = item.price
    item_update.item_name = item.item_name
    item_update.item_stock = item.item_stock

    db.commit()

    return item_update


@app.delete('/item/{item_id}')
def delete_item(item_id: int):
    item_delete = db.query(models.Item).filter(models.Item.id == item_id).first()

    if item_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_delete)
    db.commit()

    return item_delete
