import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    sku: int
    price: Decimal
    
    
# Properties to receive on item creation
class ProductCreate(ProductBase):
    pass


# Properties to receive on item update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    uploadAt: datetime.datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
