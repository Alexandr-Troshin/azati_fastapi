from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean, Float


metadata_orders = MetaData()

orders = Table(
    "orders",
    metadata_orders,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=False),
    Column("stock", String, nullable=False),
    Column("order_type", String, nullable=False),
    Column("shares", Integer, nullable=False),
    Column("price_per_share", Float, nullable=False),
    Column("order_dttm", TIMESTAMP, default=datetime.utcnow, nullable=False)
)


transactions = Table(
    "transactions",
    metadata_orders,
    Column("id", Integer, primary_key=True),
    Column("stock", String, nullable=False),
    Column("shares", Integer, nullable=False),
    Column("price_per_share", Float, nullable=False),
    Column("buyer_name", String, nullable=False),
    Column("seller_name", String, nullable=False),
    Column("transaction_dttm", TIMESTAMP, nullable=False)
)

