import asyncio
import aiohttp
import random
from aiohttp import ClientSession
from aiohttp.web_exceptions import HTTPError
import json

BASE_URL = 'http://localhost:5000'

MODEL_IDS = [0] * 10


async def get_model_props(model_id):
    url = f'{BASE_URL}/models/props/{model_id}'
    try:
        async with ClientSession() as session:
            response = await session.get(url=url)
            response.raise_for_status()
            print(f'Model props fetch status: {response.status}')
    except HTTPError as http_err:
        print(f"HTTP error occurred while fetching props: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


async def put_model_props(model_id, props):
    url = f'{BASE_URL}/models/props/{model_id}'
    try:
        for key in props:
            prop = props[key]
            if key != 'execution_key' and prop['atype'] == 'INT' and prop[
                'hival'] and prop['lowval']:
                prop['val'] = random.randint(prop['lowval'],
                                             int(prop['hival'] / 2))
        async with ClientSession() as session:
            response = await session.put(url=url, json=props)
        print(f'Model props put status: {response.status}')
    except HTTPError as http_err:
        print(f"HTTP error occurred while putting props: {http_err}")
    except Exception as err:
        print(f"An error ocurred: {err}")
    response_json = await response.json()
    return response_json


async def run_test(model_id):
    """Wrapper for running program in an asynchronous manner"""
    try:
        response_get_props = await get_model_props(model_id)
        response = await put_model_props(model_id, response_get_props)
    except Exception as err:
        print(f"Exception occured: {err}")
        pass


def start():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(
        *[run_test(model_id) for model_id in MODEL_IDS]
    ))


if __name__ == "__main__":
    start()
