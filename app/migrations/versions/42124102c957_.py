"""empty message

Revision ID: 42124102c957
Revises: ca1161b8eb3a
Create Date: 2024-10-30 21:06:04.739458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42124102c957'
down_revision: Union[str, None] = 'ca1161b8eb3a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
