from typing import Optional

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from infrastructure.database.models import User, SavedMessage, Chat
from infrastructure.database.repo.base import BaseRepo


class SavedMessageRepo(BaseRepo):
    async def get_saved_message(
        self,
        chat_id: Optional[int] = None,
        user_id: Optional[int] = None,
    ):
        """
        Gets a saved message from the database.
        :param chat_id: The chat's ID.
        :param user_id: The user's ID.
        :return: SavedMessage object, None if there was an error while making a transaction.
        """

        select_stmt = (
            select(SavedMessage)
            .where(
                (SavedMessage.chat_id == chat_id) | (SavedMessage.user_id == user_id)
            ).order_by(SavedMessage.saved_message_id)
        )
        result = await self.session.execute(select_stmt)

        await self.session.commit()
        return result.scalar_one()
