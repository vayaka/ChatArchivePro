from typing import Optional

from sqlalchemy import String
from sqlalchemy import INT, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class SavedMessage(Base, TimestampMixin, TableNameMixin):
    """
    This class represents a User in the application.
    If you want to learn more about SQLAlchemy and Alembic, you can check out the following link to my course:
    https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126

    Attributes:
        saved_message_id (Mapped[int]): The unique identifier of the saved message.
        chat_id (Mapped[int]): The unique identifier of the chat.
        original_message_id (Mapped[int]): The unique identifier of the original message.
        user_id (Mapped[int]): The unique identifier of the user.
        message_text (Mapped[str]): The text of the message.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.

    """
    saved_message_id: Mapped[int] = mapped_column(INT, primary_key=True, autoincrement=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.chat_id'))
    original_message_id: Mapped[int] = mapped_column(INT)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'))
    message_text: Mapped[str] = mapped_column(String(4096))

    chat = relationship("Chat", back_populates="saved_messages")
    user = relationship("User", back_populates="saved_messages")

    def __repr__(self):
        return f"<SavedMessage {self.saved_message_id} {self.chat_id} {self.message_text}>"
