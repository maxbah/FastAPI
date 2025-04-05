"""add items table

Revision ID: 84b3137c636f
Revises: 79d3ef49ce53
Create Date: 2025-03-30 15:55:52.444298

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b3137c636f'
down_revision: Union[str, None] = '79d3ef49ce53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('item_description', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), server_default=sa.text('0'), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('item_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###
