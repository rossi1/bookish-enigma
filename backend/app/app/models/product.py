import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.types import DECIMAL

from app.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    sku = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    uploadAt = Column(DateTime, default=datetime.datetime.utcnow)