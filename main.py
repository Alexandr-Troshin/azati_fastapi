from time import sleep, time
from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

from api.services import *


app = FastAPI(title='FASTApi Order Book')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

N_TIMES = 5
DURATION = 2

@app.get("/async_imit")
def async_imit() -> dict:
    t0 = time()
    asyncio.run(async_ml_imitation(N_TIMES, DURATION))
    print(f'Execution time for {N_TIMES} attepmts with duration {DURATION} with async def is:')
    async_exec_time = time() - t0
    print(async_exec_time)

    t0 = time()
    sync_ml_imitation(N_TIMES, DURATION)
    print(f'Execution time for {N_TIMES} attepmts with duration {DURATION} with SYNC def is:')
    sync_exec_time = time() - t0
    print(sync_exec_time)
    return {'async_exec_time': async_exec_time,
            'sync_exec_time': sync_exec_time,}


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    """Функция отображения ошибки в документации (вместо "Internal server error")"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()}),
    )





