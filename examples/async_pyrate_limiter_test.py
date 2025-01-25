import asyncio
from time import perf_counter as time
from pyrate_limiter import Duration, Limiter, RequestRate

limiter = Limiter(RequestRate(5, Duration.SECOND))
n_requests = 27

@limiter.ratelimit("test", delay=True)
async def limited_function(start_time):
    print(f"t + {(time() - start_time):.5f}")

async def test_ratelimit():
    start_time = time()
    tasks = [limited_function(start_time) for _ in range(n_requests)]
    await asyncio.gather(*tasks)
    print(f"Ran {n_requests} requests in {time() - start_time:.5f} seconds")

asyncio.run(test_ratelimit())
