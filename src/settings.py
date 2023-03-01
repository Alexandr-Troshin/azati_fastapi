"""File with settings and configs for the project"""
from envparse import Env

env = Env()

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://azati_fastapi_user:azati_fastapi_password@0.0.0.0:5433/fastapi_orders_db",
)  # connect string for the real database
