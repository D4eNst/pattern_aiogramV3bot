import asyncpg
import aioredis
import logging
from aiogram.fsm.storage.redis import RedisStorage
from .db import Database
from data.config import redis_url
from data.config import db_connection_data, postgres_db

redis = aioredis.from_url(redis_url)
storage = RedisStorage(redis=redis)


async def get_pool_connect(create_database=False) -> asyncpg.pool.Pool:
    """
        Returns a pool of database connections with data that is defined in config.py
        Make sure that you have correctly specified all the data in the .env file.
        :param create_database: creates a database named by the key "database" in db_connection_data.
        :returns: An instance of ~asyncpg.pool.Pool.
    """
    if create_database:
        logging.info("Creating database")
        user, password, db_name, host, port, *_ = db_connection_data.values()
        conn = await asyncpg.connect(user=user, password=password, database=postgres_db, host=host, port=port)
        db_exists = await conn.fetchval(
            'SELECT EXISTS(SELECT datname FROM pg_catalog.pg_database WHERE datname=$1)', db_name
        )
        if not db_exists:
            logging.info("Database is not exist")
            await conn.execute(f'CREATE DATABASE {db_name}')
        else:
            logging.info("Database already exists")
        await conn.close()

    return await asyncpg.create_pool(**db_connection_data)
