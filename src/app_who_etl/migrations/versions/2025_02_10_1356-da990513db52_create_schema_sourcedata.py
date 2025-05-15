"""create schema sourcedata

Revision ID: da990513db52
Revises: f7950a5c213d
Create Date: 2025-02-10 13:56:12.302748

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy as sa

sa.DDL

# revision identifiers, used by Alembic.
revision: str = "da990513db52"
down_revision: Union[str, None] = "f7950a5c213d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("CREATE SCHEMA IF NOT EXISTS sourcedata;"))


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("DROP SCHEMA IF EXISTS sourcedata;"))
