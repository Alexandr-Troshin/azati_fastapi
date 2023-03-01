from enum import Enum
from typing import Optional, Dict

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    user_name: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    balance: dict

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
