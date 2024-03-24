# from .models import
import logging

import asyncpg
from aiogram.fsm.storage.redis import RedisStorage
from redis import asyncio as aioredis

from data.config import settings


class Database:
    _pool_connect: asyncpg.pool.Pool = None

    @classmethod
    async def initialize_pool_connect(cls) -> asyncpg.pool.Pool:
        if cls._pool_connect is None:
            cls._pool_connect = await get_pool_connect()
        return cls._pool_connect

    @classmethod
    async def close_pool_connect(cls) -> None:
        if cls._pool_connect is not None:
            await cls._pool_connect.close()

    @property
    def pool_connect(self) -> asyncpg.pool.Pool:
        return self._pool_connect

    @classmethod
    async def create_tables(cls, pool_connect) -> None:
        async with pool_connect.acquire() as connect:
            # This is an example! Delete and create your tables
            await connect.execute(
                """
                CREATE TABLE IF NOT EXISTS table_name(
                    id INT PRIMARY KEY,
                    first INT,
                    second TEXT
                )
                """
            )


redis = aioredis.from_url(settings.redis_url)
storage = RedisStorage(redis=redis)


async def get_pool_connect() -> asyncpg.pool.Pool:
    """
        Returns a pool of database connections with data that is defined in config.py
        Make sure that you have correctly specified all the data in the .env file.
        :returns: An instance of ~asyncpg.pool.Pool.
    """

    try:
        pool_connect = await asyncpg.create_pool(settings.postgres_dsn)
    except asyncpg.exceptions.InvalidCatalogNameError:
        logging.info(f"Database with name {settings.POSTGRES_DATABASE} not found.")
        logging.info("Creating database...")

        conn = await asyncpg.connect(settings.postgres_dsn_to_main_db)
        await conn.execute(
            f"CREATE DATABASE {settings.POSTGRES_DATABASE}"
        )
        await conn.close()

        pool_connect = await asyncpg.create_pool(settings.postgres_dsn)

        await Database().create_tables(pool_connect)
        logging.info("Database has been successfully created!")

    return pool_connect
