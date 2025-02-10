"""create etl table

Revision ID: 95f38b6bd38e
Revises: 98af2865f6fc
Create Date: 2025-02-10 13:44:20.575320

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "95f38b6bd38e"
down_revision: Union[str, None] = "98af2865f6fc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.DDL(
            """
                CREATE TABLE IF NOT EXISTS etl.etl
                (
                    id int4 NOT NULL
                    GENERATED ALWAYS AS IDENTITY
                    (INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
                    starttime timestamp NOT NULL,
                    endtime timestamp NULL,
                    status varchar (10) NULL,
                    CONSTRAINT etl_pkey PRIMARY KEY(id)
                );
            """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("DROP TABLE IF EXISTS etl.etl"))
