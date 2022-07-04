import asyncio


async def get_primes_amount(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        result += 1
        for j in range(2, i):
            if i % j == 0:
                result -= 1
                break
        await asyncio.sleep(0)
    print(result)
    return result


numbers = [40000, 400, 1000000, 700]

tasks = [
    get_primes_amount(
        i,
    )
    for i in numbers
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
