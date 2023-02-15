from enum import Enum
from typing import Optional, Dict

from fastapi_users import schemas
from pydantic import BaseModel


class UserRead(schemas.BaseUser[int]):
    id: int
    user_name: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    balance: str

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    user_name: str
    email: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    balance: Optional[str] = ''
    #
    # class Config:
    #     orm_mode = True
