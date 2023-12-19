from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import Chat
from infrastructure.database.repo.base import BaseRepo


class ChatRepo(BaseRepo):
    async def get_chat(
        self,
        chat_id: Optional[int] = None,
    ):
        """
        Gets a chat from the database.
        :param chat_id: The chat's ID.
        :return: Chat object, None if there was an error while making a transaction.
        """

        select_stmt = (
            select(Chat)
            .where(
                (Chat.chat_id == chat_id)
            ).order_by(Chat.chat_id)
        )
        result = await self.session.execute(select_stmt)

        await self.session.commit()
        return result.scalar_one()
