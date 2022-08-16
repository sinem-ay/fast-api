from models import Games
from sqlalchemy import String, Integer, Column, DateTime
from database import Base, engine


def add_column(engine, table_name, column):
    column_name = column.compile(dialect=engine.dialect)
    column_type = column.type.compile(engine.dialect)
    engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type))


table_name = 'games'
column = Column('company', String(100), nullable=False)
add_column(engine, table_name, column)
