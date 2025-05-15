"""create table annualconfirmedcases

Revision ID: f7950a5c213d
Revises: 9e2772c6755f
Create Date: 2025-02-10 13:51:24.494766

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f7950a5c213d"
down_revision: Union[str, None] = "9e2772c6755f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        sa.DDL(
            """
                CREATE TABLE IF NOT EXISTS malaria.annualconfirmedcases (
                    id int4 NOT NULL GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
                    etl_id int4 NOT NULL,
                    region varchar(50) NULL,
                    regioncode varchar(10) NULL,
                    country varchar(10) NULL,
                    "year" int4 NULL,
                    cases_confirmed int4 NULL,
                    CONSTRAINT annualconfirmedcases_pkey PRIMARY KEY (id),
                    CONSTRAINT fk_etl FOREIGN KEY (etl_id) REFERENCES etl.etl(id)
                );

            """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(sa.DDL("DROP TABLE IF EXISTS malaria.annualconfirmedcases;"))
