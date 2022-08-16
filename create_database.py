from database import Base, engine
from models import Games

# Creating database
Base.metadata.create_all(engine, checkfirst=True)