# from .models import
import asyncpg


class Database:

    def __init__(self, connect: asyncpg.pool.Pool):
        self.connect = connect
        self.cursor = self.connect

    async def create_tables(self) -> None:
        await self.connect.execute("""
            CREATE TABLE IF NOT EXISTS table_name(
                id INT PRIMARY KEY,
                first INT,
                second TEXT
            )""")
