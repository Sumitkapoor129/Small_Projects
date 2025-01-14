"""Order

Revision ID: 6840d0e98fce
Revises: 9db93731fa2c
Create Date: 2024-10-04 19:47:39.628637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6840d0e98fce'
down_revision: Union[str, None] = '9db93731fa2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Orders',
    sa.Column('Order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(), nullable=False),
    sa.Column('Total', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), server_default='Placed', nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Order_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Orders')
    # ### end Alembic commands ###
