"""'deleted_completed'

Revision ID: 328239996f8e
Revises: 2c2d77765b88
Create Date: 2023-04-18 10:16:29.996145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '328239996f8e'
down_revision = '2c2d77765b88'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order history', 'completed')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order history', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
