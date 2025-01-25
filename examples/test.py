from time import time

def session_test():
    from niquests_ratelimiter import LimiterSession

    # Apply a rate limit of 5 requests per second to all requests
    session = LimiterSession(per_second=5)
    start = time()

    # Send requests that stay within the defined rate limit
    for i in range(20):
        #response = session.get('https://httpbin.org/get')
        response = session.get('https://www.naver.com')
        print(f'[t+{time()-start:.2f}] Sent request {i+1}')

def adapter_test():
    from niquests import Session
    from niquests_ratelimiter import LimiterAdapter

    session = Session()

    # Apply a rate-limit (5 requests per second) to all requests
    adapter = LimiterAdapter(per_second=5)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    start = time()

    # Send rate-limited requests
    #for user_id in range(100):
    for i in range(20):
        #response = session.get(f'https://api.some_site.com/v1/users/{user_id}')
        #print(response.json())
        response = session.get('https://www.naver.com')
        print(f'[t+{time()-start:.2f}] Sent request {i+1}')

async def async_adapter_test():
    import asyncio
    from niquests import AsyncSession
    from niquests_ratelimiter import AsyncLimiterAdapter

    session = AsyncSession()

    # Apply a rate-limit (5 requests per second) to all requests
    adapter = AsyncLimiterAdapter(per_second=5)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    start = time()

    async def fetch(i):
        response = await session.get('https://www.naver.com')
        print(f'[t+{time()-start:.2f}] Sent request {i+1}')

    # Send rate-limited requests
    #for user_id in range(100):
#    for i in range(20):
#        #response = session.get(f'https://api.some_site.com/v1/users/{user_id}')
#        #print(response.json())
#        response = await session.get('https://www.naver.com')
#        print(f'[t+{time()-start:.2f}] Sent request {i+1}')

    await asyncio.gather(*[fetch(i) for i in range(20)])

if __name__ == '__main__':
    import asyncio
    adapter_test()
    print('*'*20)
    asyncio.run(async_adapter_test())
