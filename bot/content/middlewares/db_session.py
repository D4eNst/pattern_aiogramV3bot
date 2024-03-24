from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types.base import TelegramObject

from database.db import Database


class DbSession(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data['database'] = Database()
        return await handler(event, data)
