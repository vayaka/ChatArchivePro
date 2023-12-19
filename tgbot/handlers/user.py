import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from infrastructure.database.models import User

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message, user: User):
    await message.reply(f"Привет, пользователь! {message.from_user.full_name}")
    logging.info(f"{user}")


@user_router.message(Command("help"))
async def user_start(message: Message, user: User):
    await message.reply(f"Помощь скоро будет!")
    logging.info(f"{user}")
