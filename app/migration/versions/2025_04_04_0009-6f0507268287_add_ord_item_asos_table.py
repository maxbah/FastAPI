"""add ord_item_asos table

Revision ID: 6f0507268287
Revises: 2ad7122e687a
Create Date: 2025-04-04 00:09:28.273362

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6f0507268287"
down_revision: Union[str, None] = "2ad7122e687a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_item_association",
        sa.Column("count", sa.Integer(), server_default="1", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_item_association", "count")
    # ### end Alembic commands ###
