import asyncio
from time import time, sleep

async def process_imit(duration: int) -> None:
    await asyncio.sleep(duration)


async def async_ml_imitation(n_times: int, duration: int) -> None:
    group = [process_imit(duration) for i in range(n_times)]
    await asyncio.gather(*group)
    print('async_ml_imitation done.')

def sync_ml_imitation(n_times: int, duration: int) -> None:
    for i in range(n_times):
        sleep(duration)
    print('sync_ml_imitation done.')


