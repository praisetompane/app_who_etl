"""create etl schema

Revision ID: 98af2865f6fc
Revises: 
Create Date: 2025-02-08 08:25:07.388600

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "98af2865f6fc"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("CREATE SCHEMA IF NOT EXISTS etl;"))


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("DROP SCHEMA IF EXISTS etl;"))
