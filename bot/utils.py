import logging

from database.db import Database


async def start_with() -> None:
    logging.info("Connecting to database...")
    await Database.initialize_pool_connect()

    logging.info("Successfully connected to database!")


async def stop_with():
    logging.info("Closing connection to database...")
    await Database.close_pool_connect()
    logging.info("Successfully!")

    logging.info("Bot has been stopped!")
