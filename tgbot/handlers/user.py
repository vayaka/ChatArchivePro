from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.i18n import gettext

from tgbot.filters.chat import ChatTypeFilter

user_router = Router()
user_router.message.filter(ChatTypeFilter(["private"]))


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(gettext("Старт"))


@user_router.message(Command("feedback"))
async def user_feedback(message: Message):
    await message.answer(gettext("Фидбек"))


@user_router.message(Command("help"))
async def user_start(message: Message):
    await message.answer(gettext("Помощь"))
