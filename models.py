from database import Base, engine
from sqlalchemy import String, Integer, Column, DateTime


# Create database model
class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    game_name = Column(String(40), unique=True, nullable=False)
    game_type = Column(String(40), nullable=False)
    price = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    release_date = Column(DateTime, nullable=True)
    autoload_with = engine

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


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


table_name = 'games'
column = Column('company', String(100), nullable=False)
add_column(engine, table_name, column)
