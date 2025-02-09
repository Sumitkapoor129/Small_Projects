"""image

Revision ID: 242838c5ff97
Revises: 381472f40fa0
Create Date: 2024-09-30 15:30:40.862572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '242838c5ff97'
down_revision: Union[str, None] = '381472f40fa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Products', sa.Column('image', sa.LargeBinary(length=16777216), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Products', 'image')
    # ### end Alembic commands ###
