from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Boolean


metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String, nullable=False),
    Column("email", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("balance", String,  nullable=False), #default={'money': 0}MutableDict.as_mutable(JSON)
)

