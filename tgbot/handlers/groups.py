import logging

from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message
from aiogram.utils.i18n import gettext

from infrastructure.database.models import User
from infrastructure.database.repo.requests import RequestsRepo
from tgbot.filters.chat import ChatTypeFilter

groups = Router()
groups.message.filter(ChatTypeFilter(types_chat=["group", "supergroup"]))


@groups.message(CommandStart())
async def group_user_start(message: Message, user: User):
    await message.reply(gettext("Старт"), parse_mode="html")
    logging.info(f"{user}")


@groups.message(Command("save"))
async def group_save(message: Message, command: CommandObject, repo: RequestsRepo, user: User):
    if command.args is None and message.reply_to_message is None:
        await message.reply(gettext("Нет сообщения для сохранения"), parse_mode="html")
        logging.info(f"{user} No message to save")
        return
    saved_message = await repo.saved_message.create_saved_message(chat_id=message.chat.id, user_id=user.user_id,
                                                                  original_message_id=message.message_id,
                                                                  message_text=(command.args if command.args is not None else message.reply_to_message.md_text))
    text = gettext("Сообщение:\n{text}\nОт @{username}\nСохранено!").format(text=saved_message.message_text,
                                                                            username=saved_message.user.username)
    await message.reply(text, parse_mode="html")
    logging.info(f"{user} {saved_message} Saved Message")


@groups.message(F.text.lower().startswith('запомнить') | F.text.lower().startswith('важное'))
async def group_save_text(message: Message, repo: RequestsRepo, user: User):
    saved_message = await repo.saved_message.create_saved_message(chat_id=message.chat.id, user_id=user.user_id,
                                                                  original_message_id=message.message_id,
                                                                  message_text=(message.text.lower().replace("запомнить", "")
                                                                                .replace("важное", "").strip()
                                                                                if message.reply_to_message is None
                                                                                else message.reply_to_message.text))
    text = gettext("Сообщение:\n{text}\nОт @{username}\nСохранено!").format(text=saved_message.message_text,
                                                                            username=saved_message.user.username)
    await message.reply(text, parse_mode="html")
    logging.info(f"{user} {saved_message} Saved Message")


@groups.message(Command("get"))
async def group_save(message: Message, repo: RequestsRepo, user: User):
    saved_messages = await repo.saved_message.get_saved_message(chat_id=message.chat.id)
    logging.info(f"{user} {saved_messages} Saved Message")

    text_reply = gettext("Сохраненные сообщения").format(count=len(saved_messages)) + "\n"
    for index, saved_message in enumerate(saved_messages, start=1):
        text_reply += gettext("{index}. {saved_message[0].message_text}\nСохранено @{saved_message[0].user.username}\n").format(index=index,
                                                                                                                                saved_message=saved_message)

    await message.reply(text_reply, parse_mode="html")


@groups.message(Command("help"))
async def user_start(message: Message):
    await message.reply(gettext("Помощь"), parse_mode="html")

# @groups.message()
# async def group_echo(message: Message, repo: RequestsRepo, user: User):
#     await message.reply(f"{message.text}\n{message.from_user.full_name}")
