import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo
from tgbot.filters.chat import ChatTypeFilter

groups = Router()
groups.message.filter(ChatTypeFilter(types_chat=["group", "supergroup"]))


@groups.message(CommandStart())
async def group_user_start(message: Message, user: User):
    await message.reply(f"Привет, пользователь! {message.from_user.full_name}")
    logging.info(f"{user}")


@groups.message(Command("save"))
async def group_save(message: Message, command: CommandObject, repo: RequestsRepo, user: User):
    if command.args is None:
        await message.reply("Please, enter the message to save")
        logging.info(f"{user} No message to save")
        return
    saved_message = await repo.saved_message.create_saved_message(chat_id=message.chat.id, user_id=user.user_id,
                                                                  original_message_id=message.message_id, message_text=command.args)
    await message.reply(f"Message:\n{command.args}\nBy @{message.from_user.username}\nSaved!")
    logging.info(f"{user} {saved_message} Saved Message")


@groups.message(Command("get"))
async def group_save(message: Message, repo: RequestsRepo, user: User):
    saved_messages = await repo.saved_message.get_saved_message(chat_id=message.chat.id)
    logging.info(f"{user} {saved_messages} Saved Message")

    text_reply = "Saved messages:\n"
    for index, saved_message in enumerate(saved_messages, start=1):
        text_reply += f"{index}. {saved_message[0].message_text}\nSaved by @{saved_message[0].user.username}\n"

    await message.reply(text_reply)


@groups.message(Command("help"))
async def user_start(message: Message, user: User):
    await message.reply(f"Помощь скоро будет!\n@{message.from_user.username}")
    logging.info(f"{user}")

# @groups.message()
# async def group_echo(message: Message, repo: RequestsRepo, user: User):
#     await message.reply(f"{message.text}\n{message.from_user.full_name}")
