from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_pool) -> None:
        self.session_pool = session_pool

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        async with self.session_pool() as session:
            repo = RequestsRepo(session)

            user = await repo.users.get_or_create_user(
                event.from_user.id,
                event.from_user.username,
                event.from_user.full_name,
            )

            chat = await repo.chats.get_or_create_chat(
                event.chat.id,
                event.chat.title,
            )

            data["session"] = session
            data["repo"] = repo
            data["user"] = user
            data["chat"] = chat

            result = await handler(event, data)
        return result
