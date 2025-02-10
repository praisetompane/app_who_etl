"""create table whoghomalariaannualconfirmedcases

Revision ID: 53983f446d4f
Revises: da990513db52
Create Date: 2025-02-10 14:03:12.348877

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql import text


# revision identifiers, used by Alembic.
revision: str = "53983f446d4f"
down_revision: Union[str, None] = "da990513db52"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS sourcedata.whoghomalariaannualconfirmedcases
            (
                "Id" int4 NULL,
                "IndicatorCode" varchar(20) NULL,
                "SpatialDimType" varchar(10) NULL,
                "SpatialDim" varchar(10) NULL,
                "ParentLocationCode" varchar(10) NULL,
                "ParentLocation" varchar(50) NULL,
                "TimeDimType" varchar(20) NULL,
                "TimeDim" int4 NULL,
                "Dim1Type" varchar(50) NULL,
                "Dim1" varchar(50) NULL,
                "Dim2Type" varchar(50) NULL,
                "Dim2" varchar(50) NULL,
                "Dim3Type" varchar(50) NULL,
                "Dim3" varchar(50) NULL,
                "DataSourceDimType" varchar(50) NULL,
                "DataSourceDim" varchar(50) NULL,
                "Value" varchar(50) NULL,
                "NumericValue" int4 NULL,
                "Low" varchar(50) NULL,
                "High" varchar(50) NULL,
                "Comments" varchar(100) NULL,
                "Date" timestamp NULL,
                "TimeDimensionValue" varchar(10) NULL,
                "TimeDimensionBegin" timestamp NULL,
                "TimeDimensionEnd" timestamp NULL
            );
        """
        )
    )


def downgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        text("DROP TABLE IF EXISTS sourcedata.whoghomalariaannualconfirmedcases;")
    )
