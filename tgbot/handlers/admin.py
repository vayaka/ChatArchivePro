from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.answer(f"Привет, админ! {message.from_user.full_name}")


@admin_router.message(Command("help"))
async def admin_start(message: Message):
    await message.answer(f"Помощь еще не готова!")