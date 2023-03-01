from datetime import datetime

from pydantic import BaseModel


class OrderCreate(BaseModel):
    #id: int
    #user_name: str
    stock: str
    order_type: str
    shares: int
    price_per_share: float
    #order_dttm: datetime

class TransactionCreate(BaseModel):
#    id: int
    stock: str
    shares: int
    price_per_share: float
    buyer_name: str
    seller_name: str
    transaction_dttm: datetime

