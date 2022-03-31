import asyncio

from data.RegionStat import RegionStat
from channel_url import CHANNEL_TO_URL

import aiohttp
from config import *
from data.db_session import global_init, create_session
from data.DB import DB

db = DB()


async def main():
    # Сбор статистики для ТГ каналов (один раз)
    await global_init(user=DB_LOGIN, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, dbname=DB_NAME)
    for key, value in CHANNEL_TO_URL.items():
        async with create_session() as sess:
            async with aiohttp.ClientSession() as session:
                async with session.get(value) as response:
                    html = await response.text()
                    html = html.split('<div class="tgme_page_extra">')[1]
                    data = html.split('</div>')[0]
                    members_count = data.split('members')[0][:-1]
            region = RegionStat()
            region.region_name = key
            region.members_count = members_count
            sess.add(region)
            await sess.commit()


asyncio.run(main())