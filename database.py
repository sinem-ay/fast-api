from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:sin23a@localhost/games", echo=True)


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

