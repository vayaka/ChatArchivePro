from typing import Optional

from sqlalchemy import String
from sqlalchemy import text, BIGINT, Boolean, true
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from .base import Base, TimestampMixin, TableNameMixin


class Chat(Base, TimestampMixin, TableNameMixin):
    """
    This class represents a User in the application.
    If you want to learn more about SQLAlchemy and Alembic, you can check out the following link to my course:
    https://www.udemy.com/course/sqlalchemy-alembic-bootcamp/?referralCode=E9099C5B5109EB747126

    Attributes:
        chat_id (Mapped[int]): The unique identifier of the user.
        chat_name (Mapped[Optional[str]]): The username of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.

    Inherited Attributes:
        Inherits from Base, TimestampMixin, and TableNameMixin classes, which provide additional attributes and functionality.

    Inherited Methods:
        Inherits methods from Base, TimestampMixin, and TableNameMixin classes, which provide additional functionality.

    """
    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    chat_name: Mapped[Optional[str]] = mapped_column(String(128))

    saved_messages = relationship("SavedMessage", back_populates="chat")

    def __repr__(self):
        return f"<Chat {self.chat_id} {self.chat_name}>"
