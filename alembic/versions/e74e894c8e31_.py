"""empty message

Revision ID: e74e894c8e31
Revises: 93020cbad37a
Create Date: 2025-01-02 17:16:47.902025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e74e894c8e31'
down_revision: Union[str, None] = '93020cbad37a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
