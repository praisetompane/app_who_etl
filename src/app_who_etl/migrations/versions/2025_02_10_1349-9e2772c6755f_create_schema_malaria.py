"""create schema malaria

Revision ID: 9e2772c6755f
Revises: 95f38b6bd38e
Create Date: 2025-02-10 13:49:01.899084

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e2772c6755f"
down_revision: Union[str, None] = "95f38b6bd38e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("CREATE SCHEMA IF NOT EXISTS malaria;"))


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("DROP SCHEMA IF EXISTS malaria;"))
