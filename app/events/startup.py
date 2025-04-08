import os

import aiohttp
from fastapi_utils.tasks import repeat_every

from app.currency.schemas import Symbols
from app.redis_tools.tools import RedisTool


@repeat_every(seconds= 60 * 60 * 12)
async def on_startup():
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv('ALL_PAIRS_KEY')) as resp:
            response_json = await resp.json()
            parsed_pair = Symbols(**response_json)
            cutted_pairs = parsed_pair.symbols[:20]
            symbols = [pair.symbol for pair in cutted_pairs]
            for symb in symbols:
                RedisTool.set_pair(symb, 0)


@repeat_every(seconds=5)
async def on_loop_startup():
    for symbol in RedisTool.get_keys():
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}") as resp:
                response_json = await resp.json()
                RedisTool.set_pair(symbol, response_json['price'])
