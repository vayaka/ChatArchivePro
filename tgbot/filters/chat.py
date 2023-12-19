from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    types_chat: List[str]

    def __init__(self, types_chat: List[str]) -> None:
        self.types_chat = types_chat

    async def __call__(self, obj: Message) -> bool:
        return any([obj.chat.type == type_chat for type_chat in self.types_chat])
