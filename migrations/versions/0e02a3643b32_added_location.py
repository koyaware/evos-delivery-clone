"""'added_location'

Revision ID: 0e02a3643b32
Revises: 0e51f2ca71b0
Create Date: 2023-04-17 11:20:43.111902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e02a3643b32'
down_revision = '0e51f2ca71b0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'name',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=128),
               existing_nullable=True)
    op.alter_column('products', 'desc',
               existing_type=sa.VARCHAR(length=1000),
               type_=sa.String(length=1028),
               existing_nullable=True)
    op.add_column('users', sa.Column('location_latitude', sa.String(length=256), nullable=True))
    op.add_column('users', sa.Column('location_longitude', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'location_longitude')
    op.drop_column('users', 'location_latitude')
    op.alter_column('products', 'desc',
               existing_type=sa.String(length=1028),
               type_=sa.VARCHAR(length=1000),
               existing_nullable=True)
    op.alter_column('products', 'name',
               existing_type=sa.String(length=128),
               type_=sa.VARCHAR(length=120),
               existing_nullable=True)
    # ### end Alembic commands ###
