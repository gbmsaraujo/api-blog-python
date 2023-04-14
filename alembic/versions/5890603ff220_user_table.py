"""user table

Revision ID: 5890603ff220
Revises: 55c304c750a1
Create Date: 2023-04-14 11:42:58.868870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5890603ff220"
down_revision = "55c304c750a1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
