# Hints:
# - Use asyncio.gather to run coroutines concurrently; use aiohttp for HTTP.

# Solution:
import asyncio

async def fetch_sim(n):
    await asyncio.sleep(0.01)
    return n

async def main():
    res = await asyncio.gather(*(fetch_sim(i) for i in range(5)))
    print(res)

# asyncio.run(main())  # runnable when asyncio is allowed
print('Asyncio example defined')
