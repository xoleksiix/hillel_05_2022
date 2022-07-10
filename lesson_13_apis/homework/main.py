import aiohttp
import asyncio
import random

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 400
SIZE = 9


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


async def get_random_pokemon() -> str:
    url = BASE_URL + get_random_id()

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response = await response.json()
            return response.get("name")


async def main():
    tasks = [get_random_pokemon() for _ in range(SIZE)]
    random_pokemons = await asyncio.gather(*tasks)
    print(f"Pokemons: {random_pokemons}")


if __name__ == "__main__":
    asyncio.run(main())
