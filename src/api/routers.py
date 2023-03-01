from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.models import orders
from src.api.schemas import OrderCreate
from src.auth.base_config import current_user
from src.auth.models import User
from src.database import get_async_session

router_orders =APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@router_orders.get("/")
async def get_orders(user: User = Depends(current_user),
                     session: AsyncSession = Depends(get_async_session)):
    # session, current_user = get_user_db(session)
    print(user)
    query = select(orders).where(orders.c.user_name == user.user_name)
    result = await session.execute(query)
    return {"status": f"existing orders of user {user.user_name}",
            "details": result.all()}
# TODO: пагинация ответа

@router_orders.post("/")
async def add_order(new_order: OrderCreate,
                    user: User = Depends(current_user),
                    session: AsyncSession = Depends(get_async_session)):
    order_dict = new_order.dict()
    order_dict['user_name'] = user.user_name
    stmt = insert(orders).values(**order_dict)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success",
            "details": order_dict}