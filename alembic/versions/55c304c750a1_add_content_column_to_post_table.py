"""add content column to post table

Revision ID: 55c304c750a1
Revises: e17c7ededba7
Create Date: 2023-04-14 11:34:15.987278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55c304c750a1'
down_revision = 'e17c7ededba7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
