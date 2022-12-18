import requests
import time
import asyncio
import aiohttp

URL = 'https://pokeapi.co/api/v2/'

# 1.1
def simple_print():
    resp = requests.get(f"{URL}/pokemon")
    data = resp.json()['results']
    print (data)

#1.2
async def print_pokemon(session,name):
    resp = await session.get('https://pokeapi.co/api/v2/pokemon/' + name)
    resp_json = await resp.json()
    print(f'Pokemon ', {name}, 'have a weight', {resp_json['weight']}, 'g and height', {resp_json['height']}, 'sm')

async def main():
    # 1.1
    t = time.time()
    simple_print()
    print("It took", time.time() - t, "seconds")
    # 1.2
    start = time.time()
    resp = requests.get(f"{URL}/pokemon")
    data = resp.json()['results']
    new_data= []
    for i in range(len(data)):
        new_data.append(data[i]['name'])
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[print_pokemon(session,name) for name in new_data])
    print(time.time()-start)

asyncio.run(main())