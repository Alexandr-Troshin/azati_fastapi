import json
from typing import Optional

from fastapi import Depends, Request
from fastapi.encoders import jsonable_encoder
from fastapi_users import BaseUserManager, IntegerIDMixin, exceptions, models, schemas

from src.auth.models import User
#from src.auth.schemas import UserFund
from src.auth.utils import get_user_db
from src.config import SECRET_KEY

SECRET = SECRET_KEY


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create: schemas.UC,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)
        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
        password = user_dict.pop("password")
        user_dict["hashed_password"] = self.password_helper.hash(password)
        try:
            user_dict["balance"] = {'money': 0}
            # print(user_dict)
        except Exception as e:
            print(e)
            raise exceptions

        created_user = await self.user_db.create(user_dict)
        # print(created_user.__dict__)
        await self.on_after_register(created_user, request)

        return created_user


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)