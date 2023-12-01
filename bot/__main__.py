import asyncio
import logging

from aiogram.methods import DeleteWebhook

from database import get_pool_connect
from .bot import dp, bot
from .content.handlers import rg_msg_hd
from .content.middlewares import rg_middlewares
from .utils import start_with, stop_with

logging.basicConfig(level=logging.INFO)


async def start_bot():
    # register handlers and start/stop functions
    dp.startup.register(start_with)
    dp.shutdown.register(stop_with)

    # getting main pool connect
    pool_connect = await get_pool_connect()
    if pool_connect is None:
        return

    rg_msg_hd(dp)
    rg_middlewares(dp, pool_connect)

    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await pool_connect.close()
        await bot.session.close()

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
