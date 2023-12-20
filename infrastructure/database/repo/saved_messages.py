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
        return result.fetchall()

    async def create_saved_message(
            self,
            chat_id: int = None,
            user_id: int = None,
            original_message_id: int = None,
            message_text: str = "",
    ) -> Optional[SavedMessage]:
        """
        Creates a saved message in the database.
        :param chat_id: The chat's ID.
        :param user_id: The user's ID.
        :param original_message_id: The original message's ID.
        :param message_text: The message's text.
        :return: SavedMessage object, None if there was an error while making a transaction.
        """

        insert_stmt = insert(SavedMessage).values(
            chat_id=chat_id,
            user_id=user_id,
            original_message_id=original_message_id,
            message_text=message_text,
        ).returning(SavedMessage)
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one_or_none()
