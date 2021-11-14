"""Removes nullable from blog id column

Revision ID: f2e576c327d0
Revises: 399ff4d80c6d
Create Date: 2021-11-14 08:19:18.651905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2e576c327d0'
down_revision = '399ff4d80c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'blog_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###