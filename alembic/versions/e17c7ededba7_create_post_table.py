"""create post table

Revision ID: e17c7ededba7
Revises:
Create Date: 2023-04-14 11:11:59.203160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e17c7ededba7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "posts",
        sa.Column("id", sa.INTEGER(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
