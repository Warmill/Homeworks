import asyncio
import aiohttp

URL = 'https://pokeapi.co/api/v2/type/'

#1.2
async def get_pokemons_by_type(session,types):
    resp = await session.get(URL + types)
    resp_json = await resp.json()
    return resp_json

async def print_pokemons (session, data):
    pika = []
    for i in range(len(data)):
        for j in data[i]['pokemon']:
            name = j.get('pokemon').get('name')
            id = j.get('pokemon').get('url').split('/', 1)[-1].split('/')[-2]
            respir = await session.get('https://pokeapi.co/api/v2/pokemon/' + name)
            resp_js = await respir.json()
            res = 'id:', id, 'name:', name, 'weight:', resp_js['weight'], 'height:', resp_js['height']
            pika.append(res)
    return pika

async def main():
    poke_type= input('What type of pokemon you want to download? ')
    async with aiohttp.ClientSession() as session:
        data = await asyncio.gather(*[get_pokemons_by_type(session,poke_type)])
        result = await asyncio.gather(*[print_pokemons(session,data)])
    print (result)


asyncio.run(main())