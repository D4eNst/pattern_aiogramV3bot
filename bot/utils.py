import logging
from database import get_pool_connect, Database


async def start_with() -> None:
    """
        The function that is executed when the bot starts. Initially connects to the database
        (if there is no database, it will be created earlier in <url>)
        and creates tables described in the create_tables function.\n
        The function can be expanded.\n
        The function does not accept parameters.
        :returns: The function should not return anything
    """
    try:
        logging.info("Creating tables")
        pool_connect = await get_pool_connect(create_database=False)
        async with pool_connect.acquire() as connect:
            db = Database(connect)
            await db.create_tables()
        await pool_connect.close()

    except ConnectionRefusedError:
        logging.error("Error in creating pool. Make sure that the database is connected and the pool data is "
                      "specified correctly (data/config.py)")
        return
    logging.info("database has been connected")
    logging.warning("Bot has been started!")


async def stop_with():
    logging.warning("Bot has been stopped!")
