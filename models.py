from database import Base
from sqlalchemy import String, Integer, Column, DateTime


# Create database model
class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    game_name = Column(String, unique=True, nullable=False)
    game_type = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<Game name={self.game_name} price={self.price}>"


class Ranking(Base):
    __tablename__ = 'ranking'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    game_name = Column(String, unique=True, nullable=False)
    rank_site = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)


class PersonalRanking(Base):
    __tablename__ = 'personalRanking'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    game_name = Column(String, unique=True, nullable=False)
    rank = Column(Integer, nullable=False)
