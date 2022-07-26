from database import Base, engine
from models import Item

# Creating database
Base.metadata.create_all(engine)
