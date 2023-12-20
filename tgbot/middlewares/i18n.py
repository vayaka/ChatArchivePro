from typing import Callable, Dict, Any, Awaitable

from aiogram.utils.i18n.middleware import I18nMiddleware
from aiogram.types import Message, TelegramObject


class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        if data['user'] is None:
            return 'ru'
        return data['user'].language
