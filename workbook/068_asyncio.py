# Example 68: Asyncio basics
# Topics: async/await, asyncio
import asyncio

async def say(msg):
    await asyncio.sleep(0.1)
    print(msg)

async def main():
    await asyncio.gather(say('a'), say('b'))

# asyncio.run(main())  # commented for safe example

# Task: write an async function that fetches URLs concurrently
