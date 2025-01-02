"""empty message

Revision ID: 7bc01086d58c
Revises: e74e894c8e31
Create Date: 2025-01-02 17:21:56.884015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bc01086d58c'
down_revision: Union[str, None] = 'e74e894c8e31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
