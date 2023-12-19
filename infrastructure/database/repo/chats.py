from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Chat
from infrastructure.database.repo.base import BaseRepo


class ChatRepo(BaseRepo):
    async def get_or_create_chat(
            self,
            chat_id: int = None,
            chat_name: str = ""
    ):
        """
        Gets or creates a chat in the database.
        :param chat_id: The chat's ID.
        :param chat_name: The chat's name.
        :return: Chat object, None if there was an error while making a transaction.
        """

        insert_stmt = (
            insert(Chat)
            .values(
                chat_id=chat_id,
                chat_name=chat_name,
            )
            .on_conflict_do_update(
                index_elements=[Chat.chat_id],
                set_=dict(
                    chat_name=chat_name,
                ),
            )
            .returning(Chat)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one_or_none()
