from fastapi import FastAPI, status, HTTPException, Request
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models
import time
from loguru import logger
from datetime import datetime

app = FastAPI()

logger.add("file_1.log",backtrace=True, diagnose=True, rotation="500 MB")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# Creating schema/model item class with pydantic
class Games(BaseModel):
    id: int
    game_name: str
    game_type: str
    price: int
    country: str
    release_date: datetime

    class Config:
        orm_mode = True  # Sql objects to json

class Ranking(BaseModel):
    id: int
    game_name: str
    rank_site: str
    rank: int

    class Config:
        orm_mode = True

class PersonalRanking(BaseModel):
    id: int
    game_name: str
    rank: int

    class Config:
        orm_mode = True


db = SessionLocal()

@logger.catch
@app.get('/games', response_model=List[Games], status_code=status.HTTP_200_OK)
def get_all_games():
    try:
        return db.query(models.Games).all()
    except ZeroDivisionError:
        logger.exception("Error")


@app.get('/game/{game_id}', response_model=Games, status_code=status.HTTP_200_OK)
def get_game(game_id: int):
    return db.query(models.Games).filter(models.Games.id == game_id).first()


@app.post('/game/', response_model=Games, status_code=status.HTTP_201_CREATED)
def create_game(game: Games):
    db_game = db.query(models.Games).filter(models.Games.game_name == game.game_name).first()

    if db_game is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_game = models.Games(
        id=game.id,
        game_name=game.game_name,
        game_type=game.game_type,
        price=game.price,
        country=game.country
    )

    db.add(new_game)
    db.commit()

    return new_game


@app.put('/game/{game_id}', response_model=Games, status_code=status.HTTP_200_OK)
def update_game(game_id: int, game: Games):
    game_update = db.query(models.Games).filter(models.Games.id == game_id).first()

    game_update.game_name = game.game_name
    game_update.game_type = game.game_type
    game_update.price = game.price
    game_update.country = game.country

    db.commit()

    return game_update


@app.delete('/game/{game_id}')
def delete_game(game_id: int):
    game_delete = db.query(models.Games).filter(models.Games.id == game_id).first()

    if game_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(game_delete)
    db.commit()

    return game_delete
