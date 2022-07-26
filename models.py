from database import Base
from sqlalchemy import String, Boolean, Integer, Column


# Create database model
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    item_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    item_stock = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<Item name={self.item_name} price={self.price}>"
