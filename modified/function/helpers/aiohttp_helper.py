# https://github.com/pokurt/Nana-Remix/blob/5ec27fcc124e7438b2816731c07ea4a129dc9a4d/nana/utils/aiohttp_helper.py#L4
# ported from nana remix

import aiohttp


session = aiohttp.ClientSession()
mod_aiohttp = session.get(link)


async def fetch_json(link):
    async with mod_aiohttp as resp:
        return await resp.json()

class AioHttp:
    @staticmethod
    async def get_json(link):
            async with mod_aiohttp as resp:
                return await resp.json()

    @staticmethod
    async def get_text(link):
            async with mod_aiohttp as resp:
                return await resp.text()

    @staticmethod
    async def get_raw(link):
            async with mod_aiohttp as resp:
                return await resp.read()
