"""Add language to User

Revision ID: 79c205aaaa78
Revises: 224602685109
Create Date: 2023-12-20 17:19:51.329765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '79c205aaaa78'
down_revision: Union[str, None] = '224602685109'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('language', sa.String(length=10), server_default=sa.text("'en'"), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'language')
    # ### end Alembic commands ###
